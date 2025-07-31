from rest_framework import serializers
from .models import *

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        

class SerialNumberSerializer(serializers.ModelSerializer):
    work_order = serializers.SlugRelatedField(
        slug_field='workorder',
        queryset=WorkOrder.objects.all()
    )

    class Meta:
        model = SN_Master
        fields = [
            'id',
            'work_order',
            'sn',
            'cdate',
            'last_update',
            'current_opid',
            'current_routing_id',
            'prev_station',
            'current_station',
            'next_station',
            'uuid',
            'status',
        ]
        read_only_fields = ['id', 'cdate', 'last_update']