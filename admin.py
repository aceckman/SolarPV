from django.contrib import admin
from .models import Product,Certificate,Service

@admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['model_ID', 'name', 'celltech', 'cellman', 'numcells', 'numcells_series', 'numseries_strings', 'numdiodes', 'product_length', 'product_width', 'product_weight', 'subtype']
	list_filter = ['model_ID', 'name', 'celltech', 'cellman', 'numcells', 'numcells_series', 'numseries_strings', 'numdiodes', 'product_length', 'product_width', 'product_weight', 'subtype']
	fields = [('model_ID', 'name'), 'celltech', 'cellman', 'numcells', 'numcells_series', 'numseries_strings', 'numdiodes', 'product_length', 'product_width', 'product_weight', 'subtype']

@admin.site.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ['certificate_ID', 'certificate_num', 'location_ID', 'reportnum', 'user_ID', 'teststand_ID', 'product_ID', 'certissue_date']
	list_filter = ['certificate_ID', 'certificate_num', 'location_ID', 'reportnum', 'user_ID', 'teststand_ID', 'product_ID', 'certissue_date']
	fields = [('certificate_ID', 'certificate_num'), 'location_ID', 'reportnum', 'user_ID', 'teststand_ID', 'product_ID', 'certissue_date']

@admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['service_ID', 'servicename', 'description', 'FIrequirement', 'FIfrequency', 'teststand_ID']
	list_filter = ['service_ID', 'servicename', 'description', 'FIrequirement', 'FIfrequency', 'teststand_ID']
	fields =  [('service_ID', 'servicename'), 'description', 'FIrequirement', 'FIfrequency', 'teststand_ID']
