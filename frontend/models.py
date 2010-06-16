from django.db import models

# storeIt Service consummers
class Consummer(models.Model):
	STATUS_CHOICES = (
				('A', 'Active'),
				('I', 'Inactive'),
			)
	name = models.CharField(max_length=50, unique=True)
	api_key = models.CharField(max_length=50)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

# In practice a bucket is like a 'directory' where you can store your assets.
# You can organize assets collections in a bucket.
# Typically 'one bucket per project' is a good option.
class Bucket(models.Model):
	STATUS_CHOICES = (
				('P', 'Public'),
				('X', 'Private'),
			)
	name = models.CharField(max_length=50, unique=True)								# Convenient name for REST route (@see slug field in django ?)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	consummer = models.ForeignKey(Consummer)

# Attachable assets transformations
# TODO : think about 'chainable' behaviours, like generating 
# 3 thumbs for an image in 3 different sizes
class Behavior(models.Model):
	name = models.CharField(max_length=50, unique=True)								# Convenient name for REST route (@see slug field in django ?)
	task_name = models.CharField(max_length=50)							 					# from .ini enabled plugins list
	task_parameters = models.CharField(max_length=250) 								# store params serialized way (json ?)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	consummer = models.ForeignKey(Consummer)
