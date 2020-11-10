from django.db import models

class Client(models.Model):
	client_ID = models.IntegerField()
	clientcode = models.IntegerField()
	clientname = models.CharField(max_length=20)
	clienttype = models.CharField(max_length=20)

	def __str__(self):
		return self.client_ID

class User(models.Model):
	user_ID = models.IntegerField()
	client_ID = models.ManyToManyField(Client)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	middlename = models.CharField(max_length=20)
	jobtitle = models.CharField(max_length=50)
	email = models.EmailField()
	officephone = models.CharField(max_length=20)
	cellphone = models.CharField(max_length=20)
	prefix = models.CharField(max_length=20)
	isstaff = models.CharField(max_length=20)

	def __str__(self):
		return self.user_ID

class Location(models.Model):
	location_ID = models.IntegerField()
	client_ID = models.ManyToManyField(Client)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	postalcode = models.IntegerField()
	country = models.CharField(max_length=20)
	phonenum = models.IntegerField()
	faxnum = models.IntegerField()

	def __str__(self):
		return self.location_ID

class TestStandard(models.Model):
	teststand_ID = models.IntegerField()
	standardname = models.CharField(max_length=20)
	description = models.TextField()
	pubdate = models.DateField()

	def __str__(self):
		return self.teststand_ID

class Service(models.Model):
	service_ID = models.IntegerField()
	servicename = models.CharField(max_length=50)
	description = models.TextField()
	FIrequirement = models.CharField(max_length=20)
	FIfrequency = models.CharField(max_length=15)
	teststand_ID = models.ManyToManyField(TestStandard)

	def __str__(self):
		return self.service_ID

class Product(models.Model):
	model_ID = models.IntegerField()
	name =  models.CharField(max_length=20)
	celltech = models.TextField()
	cellman = models.TextField()
	numcells = models.IntegerField()
	numcells_series = models.IntegerField()
	numseries_strings = models.IntegerField()
	numdiodes = models.IntegerField()
	product_length = models.CharField(max_length=20)
	product_width = models.CharField(max_length=20)
	product_weight = models.CharField(max_length=20)
	subtype = models.CharField(max_length=20)

	def __str__(self):
		return self.model_ID

class PerformanceData(models.Model):
	model_ID = models.ManyToManyField(Product)
	test_seq = models.CharField(max_length=50)
	maxsys_volt = models.CharField(max_length=50)
	opencirc_volt = models.CharField(max_length=50)
	short_circ = models.CharField(max_length=50)
	max_volt = models.CharField(max_length=20)
	max_power = models.CharField(max_length=20)
	max_output = models.CharField(max_length=20)
	fillfactor = models.TextField()

	def __str__(self):
		return self.test_seq

class TestSequence(models.Model):
	sequence_ID = models.IntegerField()
	sequence_name = models.CharField(max_length=50)

	def __str__(self):
		return self.sequence_ID

class ProductFactory(models.Model):
	location_ID = models.ManyToManyField(Location)
	product_ID = models.ManyToManyField(Product)
	user_ID = models.ManyToManyField(User)

	def __str__(self):
		return self.user_ID

class Certificate(models.Model):
	certificate_ID = models.IntegerField()
	certificate_num = models.IntegerField()
	location_ID = models.ManyToManyField(Location)
	reportnum = models.IntegerField()
	user_ID = models.ManyToManyField(User)
	teststand_ID = models.ManyToManyField(TestStandard)
	product_ID = models.ManyToManyField(Product)
	certissue_date = models.DateField()

	def __str__(self):
		return self.certificate_ID

class FactoryInspection(models.Model):
	factory_ID = models.IntegerField()
	location_ID = models.ManyToManyField(Location)
	report_num = models.IntegerField()
	date = models.DateField()
	inspector_ID = models.IntegerField()
	inspection_seq = models.CharField(max_length=20)
	certificate_num = models.ManyToManyField(Certificate)
	findings = models.TextField()

	def __str__(self):
		return self.factory_ID