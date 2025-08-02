from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WorkOrder
from .serializers import *
from rest_framework import status

class WorkOrderListView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    search_fields = ['workorder']

    def get(self, request):
        search = request.query_params.get('search')
        if search:
            queryset = self.queryset.filter(workorder=search)
            if queryset.exists():
                serializer = WorkOrderSerializer(queryset.first())
                print(serializer.data)
                return Response(serializer.data)
            else:
                return Response({'error': 'Data not found'}, status=404)
        else:
            return Response({'error': 'Search parameter is required'}, status=400)
        
class SerialNumberView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_query = request.query_params.get('search', None)

        if search_query:
            serials = SN_Master.objects.filter(work_order__workorder=search_query)
        else:
            serials = SN_Master.objects.all()

        serializer = SerialNumberSerializer(serials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SerialNumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        sns = request.data.get('sn')  # expecting a list of serial numbers
        work_order = request.data.get('work_order')

        if not sns or not work_order:
            return Response(
                {"detail": "'sn' (list) and 'work_order' are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(sns, list):
            return Response(
                {"detail": "'sn' must be a list of serial numbers."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serials_to_delete = SN_Master.objects.filter(sn__in=sns, work_order__workorder=work_order)

        count = serials_to_delete.count()
        if count == 0:
            return Response({"detail": "No matching serial numbers found."}, status=status.HTTP_404_NOT_FOUND)

        serials_to_delete.delete()

        return Response({"detail": f"Deleted {count} serial number(s)."}, status=status.HTTP_204_NO_CONTENT)