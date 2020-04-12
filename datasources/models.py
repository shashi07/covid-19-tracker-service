from django.db import models

# Create your models here.


class BaseData(models.Model):

    country = models.CharField(max_length=100)
    confirmed_cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    date = models.DateTimeField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country + "-" + str(self.confirmed_cases)
