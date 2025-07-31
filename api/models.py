from django.db import models
from datetime import datetime
# Create your models here.

class Project_master(models.Model):
	project = models.CharField(max_length=40, blank=True, null=True,default='')  # Field name made lowercase.
	customer_project = models.CharField(max_length=40, blank=True, null=True,default='')  # Field name made lowercase.
	plant = models.CharField(max_length=5, blank=True, null=True,default='')  # Field name made lowercase.
	description = models.CharField(max_length=120, blank=True, null=True,default='')
	formatmask = models.CharField(max_length=120, blank=True, null=True,default='')  # Field name made lowercase.
	formatmask_pack = models.CharField(max_length=120, blank=True, null=True,default='')  # Field name made lowercase.
	carton_min_weigth = models.CharField(max_length=10,blank=True, null=True,default='0')  # Field name made lowercase.
	carton_max_weigth = models.CharField(max_length=10,blank=True, null=True,default='0')   # Field name made lowercase.
	giftbox_min_weigth = models.CharField(max_length=10,blank=True, null=True,default='0')   # Field name made lowercase.
	giftbox_max_weigth = models.CharField(max_length=10,blank=True, null=True,default='0')   # Field name made lowercase.
	remark = models.CharField(max_length=120, blank=True, null=True,default='')  # Field name made lowercase.
	create_date = models.CharField(max_length=25, blank=True, null=True,default='')  # Field name made lowercase.
	date = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
	qty_per_box = models.CharField(max_length=25, blank=True, null=True,default='')  # Field name made lowercase.
	thr_prepacking = models.IntegerField(default=1, blank=True)  # Field name made lowercase.
	mix_workorder = models.BooleanField(default=False)
	require_register_sn = models.BooleanField(default=True)
	def __str__(self):
		return '%s' % (self.project)

class Project_detail(models.Model):
	project_master = models.ForeignKey(Project_master,related_name='Project_master', max_length=25,null=True, blank=True,on_delete=models.CASCADE)
	component = models.CharField(max_length=20, blank=True, null=True,default='')  # Field name made lowercase.
	qty = models.CharField(max_length=4, blank=True, null=True,default='')  # Field name made lowercase.
	boxbuild = models.CharField(max_length=15, blank=True, null=True,default='')  # Field name made lowercase.
	need_validate_sn = models.BooleanField(default=False)  # Field name made lowercase.
	validate_sn_type = models.CharField(max_length=25, blank=True, null=True,default='') # Field name made lowercase.
	def __str__(self):
		return '%s' % (self.project_master)

class WorkOrder(models.Model):
    workorder = models.CharField(max_length=20)
    project = models.CharField(max_length=50)
    qty = models.IntegerField(default=0,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.workorder) 
    
class SN_Master(models.Model):
	work_order = models.ForeignKey(WorkOrder,related_name='WorkOrder_sn', max_length=10,null=True, blank=True,on_delete=models.CASCADE)
	cdate = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
	last_update = models.DateTimeField(blank=True, null=True,auto_now=True)  # Field name made lowercase.
	sn = models.CharField(max_length=100, blank=True, null=True,default='')  # Field name made lowercase.
	current_opid = models.CharField(max_length=10, blank=True, null=True,default='')  # Field name made lowercase.
	current_routing_id = models.CharField(max_length=10, blank=True, null=True,default='')  # Field name made lowercase.
	prev_station = models.CharField(max_length=40, blank=True, null=True,default='')
	current_station = models.CharField(max_length=40, blank=True, null=True,default='')
	next_station = models.CharField(max_length=40, blank=True, null=True,default='')
	uuid = models.CharField(max_length=50, blank=True, null=True,default='')
	status = models.CharField(max_length=1, blank=True, null=True,default='')
	def __str__(self):
		return '%s' % (self.sn) 
	class Meta:
		unique_together = (("work_order", "sn"),)