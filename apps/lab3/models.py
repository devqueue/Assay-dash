from django.db import models
from apps.home.models import Samples, Utilization, Revenue, MissedRevenue, stats, monthlystats, Csv

# Create your models here.

class Samples(Samples):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class Utilization(Utilization):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class Revenue(Revenue):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class MissedRevenue(MissedRevenue):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class stats(stats):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class monthlystats(monthlystats):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class Csv(Csv):
    pass