from django.db import models
from apps.home.models import Samples, Utilization, Revenue, MissedRevenue, stats, monthlystats, Csv

# Create your models here.

class Samples(Samples):
    pass

class Utilization(Utilization):
    AssayID = models.CharField(max_length=50)
    MachineID = models.CharField(primary_key=True, max_length=100)

class Revenue(Revenue):
    AssayID = models.CharField(max_length=50)
    MachineID = models.CharField(primary_key=True, max_length=100)

class MissedRevenue(MissedRevenue):
    AssayID = models.CharField(max_length=50)
    MachineID = models.CharField(primary_key=True, max_length=100)

class stats(stats):
    AssayID = models.CharField(max_length=50)
    MachineID = models.CharField(primary_key=True, max_length=100)

class monthlystats(monthlystats):
    AssayID = models.CharField(max_length=50)
    MachineID = models.CharField(primary_key=True, max_length=100)

class Csv(Csv):
    pass