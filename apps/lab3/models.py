from django.db import models
from apps.home.models import Samples, Utilization, Revenue, MissedRevenue, stats, monthlystats, Csv

# Create your models here.

class Samples(Samples):
    pass

class Utilization(Utilization):
    pass

class Revenue(Revenue):
    pass

class MissedRevenue(MissedRevenue):
    pass

class stats(stats):
    pass

class monthlystats(monthlystats):
    pass

class Csv(Csv):
    pass