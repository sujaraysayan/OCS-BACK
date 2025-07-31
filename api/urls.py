from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

# router = DefaultRouter()
# router.register('apiPOOutstandingSearching', POOutstandingViewSet,'apiPOOutstandingSearching')
# router.register('apiPOForeCastSearching', POForeCastViewSet,'apiPOForeCastSearching')

urlpatterns = [
    path('workorder/', view=WorkOrderListView.as_view(), name='get_workorder'),
    path('serialnumber/', view=SerialNumberView.as_view(), name='serialnumber'),
]
