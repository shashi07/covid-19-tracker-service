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


class StateRefreshData(models.Model):

    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=True, blank=True)
    confirmed_cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    as_of_date = models.DateTimeField()

    def __str__(self):
        return self.state + "-" +self.district + "-" + str(self.confirmed_cases)


class ConsolidatedData(models.Model):

    entity = models.CharField(max_length=100)
    confirmed_cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    as_of_date = models.DateTimeField()

    def __str__(self):
        return self.entity + "-" + str(self.confirmed_cases)


class ComparisionData(models.Model):

    variable = models.CharField(max_length=100)
    world = models.CharField(max_length=100)
    india = models.CharField(max_length=100)
    maharashtra = models.CharField(max_length=100)
    as_of_date = models.DateTimeField()

    def __str__(self):
        return self.variable + "-" + str(self.world)


class StateWiseData(models.Model):

    state = models.CharField(max_length=100)
    cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    mortality = models.FloatField(default=0.0)
    as_of_date = models.DateTimeField()

    def __str__(self):
        return self.state + "-" + str(self.cases)


class AgeWiseData(models.Model):

    age_group = models.CharField(max_length=100)
    cases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    mortality = models.FloatField(default=0.0)
    as_of_date = models.DateTimeField()

    def __str__(self):
        return self.age_group + "-" + str(self.cases)