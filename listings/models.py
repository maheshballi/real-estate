from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title =models.CharField(max_length=200)
  address =models.CharField(max_length=200)
  city =models.CharField(max_length=100)
  state =models.CharField(max_length=100)
  zipcode =models.CharField(max_length=20)
  description =models.TextField(blank=True)
  price =models.IntegerField()
  bedrooms =models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo1_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo2_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo3_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo4_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo5_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo6_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title
