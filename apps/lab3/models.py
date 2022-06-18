from django.db import models
from apps.home.models import Samples, Utilization, Revenue, MissedRevenue, stats, monthlystats, Csv

# Create your models here.

class SamplesMachine(Samples):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class SamplesAssay(Samples):
    AssayID = models.CharField(primary_key=True, max_length=100)
    MachineID = None


class UtilizationMachine(Utilization):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class UtilizationAssay(Utilization):
    AssayID = models.CharField(primary_key=True, max_length=100)
    MachineID = None

class RevenueMachine(Revenue):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class RevenueAssay(Revenue):
    AssayID = models.CharField(primary_key=True, max_length=100)
    MachineID = None

class MissedRevenueMachine(MissedRevenue):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class MissedRevenueAssay(MissedRevenue):
    AssayID = models.CharField(primary_key=True, max_length=100)
    MachineID = None

class statsMachine(stats):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class statsAssay(stats):
    AssayID = models.CharField(primary_key=True, max_length=50)
    MachineID = None
 

class monthlystatsMachine(monthlystats):
    AssayID = None
    MachineID = models.CharField(primary_key=True, max_length=100)

class monthlystatsAssay(monthlystats):
    AssayID = models.CharField(primary_key=True, max_length=100)
    MachineID = None

class Csv(Csv):
    pass