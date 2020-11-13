from rest_framework import serializers
from .models import Product,Certificate,Service

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('model_ID', 'name', 'celltech', 'cellman', 'numcells', 'numcells_series', 'numseries_strings', 'numdiodes', 'product_length', 'product_width', 'product_weight', 'subtype')

class CertificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		fields = ('certificate_ID', 'certificate_num', 'location_ID', 'reportnum', 'user_ID', 'teststand_ID', 'product_ID', 'certissue_date')

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ('service_ID', 'servicename', 'description', 'FIrequirement', 'FIfrequency', 'teststand_ID')