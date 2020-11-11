from django.db import models

class Client(models.Model):
	client_ID = models.CharField(max_length=20)
	clientcode = models.CharField(max_length=20)
	clientname = models.CharField(max_length=20)
	clienttype = models.CharField(max_length=20)

	def __str__(self):
		return self.client_ID

class User(models.Model):
	user_ID = models.CharField(max_length=20)
	client_ID = models.ManyToManyField(Client)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	middlename = models.CharField(max_length=20)
	jobtitle = models.CharField(max_length=50)
	email = models.CharField(max_length=20)
	officephone = models.CharField(max_length=20)
	cellphone = models.CharField(max_length=20)
	prefix = models.CharField(max_length=20)
	isstaff = models.CharField(max_length=20)

	def __str__(self):
		return self.user_ID

class Location(models.Model):
	location_ID = models.CharField(max_length=20)
	client_ID = models.ManyToManyField(Client)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	postalcode = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	phonenum = models.CharField(max_length=20)
	faxnum = models.CharField(max_length=20)

	def __str__(self):
		return self.location_ID

class TestStandard(models.Model):
	teststand_ID = models.CharField(max_length=20)
	standardname = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	pubdate = models.DateField()

	def __str__(self):
		return self.teststand_ID

class Service(models.Model):
	service_ID = models.CharField(max_length=20)
	servicename = models.CharField(max_length=50)
	description = models.TextField()
	FIrequirement = models.CharField(max_length=20)
	FIfrequency = models.CharField(max_length=15)
	teststand_ID = models.ManyToManyField(TestStandard)

	def __str__(self):
		return self.service_ID

class Product(models.Model):
	model_ID = models.CharField(max_length=20)
	name =  models.CharField(max_length=20)
	celltech = models.TextField()
	cellman = models.TextField()
	numcells = models.CharField(max_length=20)
	numcells_series = models.CharField(max_length=20)
	numseries_strings = models.CharField(max_length=20)
	numdiodes = models.CharField(max_length=20)
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
	sequence_ID = models.CharField(max_length=20)
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
	certificate_ID = models.CharField(max_length=20)
	certificate_num = models.CharField(max_length=20)
	location_ID = models.ManyToManyField(Location)
	reportnum = models.CharField(max_length=20)
	user_ID = models.ManyToManyField(User)
	teststand_ID = models.ManyToManyField(TestStandard)
	product_ID = models.ManyToManyField(Product)
	certissue_date = models.DateField()

	def __str__(self):
		return self.certificate_ID

class FactoryInspection(models.Model):
	factory_ID = models.CharField(max_length=20)
	location_ID = models.ManyToManyField(Location)
	report_num = models.CharField(max_length=20)
	date = models.DateField()
	inspector_ID = models.CharField(max_length=20)
	inspection_seq = models.CharField(max_length=20)
	certificate_num = models.ManyToManyField(Certificate)
	findings = models.TextField()

	def __str__(self):
		return self.factory_ID