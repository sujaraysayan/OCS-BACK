from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.


class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('workorder', 'project', 'qty', 'description', 'created_at')
    search_fields = ('workorder', 'project', 'description')

class Project_masterAdmin(admin.ModelAdmin):
    list_display = ('project', 'customer_project', 'plant', 'description', 'create_date')
    search_fields = ('project', 'customer_project', 'description')

class Project_detailAdmin(admin.ModelAdmin):
    list_display = ('project_master', 'component', 'qty', 'boxbuild', 'need_validate_sn', 'validate_sn_type')
    search_fields = ('project_master', 'component', 'validate_sn_type')

class SN_MasterAdmin(admin.ModelAdmin):
    list_display = ('work_order', 'cdate', 'last_update', 'sn', 'current_opid', 'current_routing_id', 'prev_station', 'current_station', 'next_station', 'uuid', 'status')
    search_fields = ('work_order', 'sn', 'current_opid', 'current_routing_id', 'prev_station', 'current_station', 'next_station', 'uuid', 'status')

admin.site.register(Project_master, Project_masterAdmin)
admin.site.register(Project_detail  , Project_detailAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(SN_Master, SN_MasterAdmin)
    