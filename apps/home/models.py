# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
import datetime
# Create your models here.


def current_year():
    return datetime.date.today().year


class Samples(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)
    class Meta:
        abstract = True


class Utilization(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)
    class Meta:
        abstract = True


class Revenue(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)
    class Meta:
        abstract = True


class MissedRevenue(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    Assay = models.CharField(max_length=100)
    January = models.FloatField()
    February = models.FloatField()
    March = models.FloatField()
    April = models.FloatField()
    May = models.FloatField()
    June = models.FloatField()
    July = models.FloatField()
    August = models.FloatField()
    September = models.FloatField()
    October = models.FloatField()
    November = models.FloatField()
    December = models.FloatField()
    Year = models.IntegerField(default=current_year)
    class Meta:
        abstract = True


class stats(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    FullCapacity = models.FloatField()
    RunTime = models.FloatField()
    Price = models.FloatField()
    Maintenance = models.FloatField()
    class Meta:
        abstract = True


class monthlystats(models.Model):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = models.CharField(max_length=100)
    MaxMonthlyhours = models.FloatField()
    MaxMonthlyRevenue = models.FloatField()
    MaxMonthSamples = models.FloatField()
    class Meta:
        abstract = True


class Csv(models.Model):
    file_ID = models.AutoField(primary_key=True)
    file_name = models.FileField(upload_to='upload')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"File: {self.file_name}"
    class Meta:
        abstract = True
