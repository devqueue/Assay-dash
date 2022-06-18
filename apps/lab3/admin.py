from django.contrib import admin
from .models import SamplesMachine, RevenueMachine, UtilizationMachine, statsMachine, monthlystatsMachine, MissedRevenueMachine, SamplesAssay, UtilizationAssay, RevenueAssay, statsAssay, monthlystatsAssay, MissedRevenueAssay, Csv
# Register your models here.
admin.site.register([SamplesMachine, RevenueMachine, UtilizationMachine,
                    statsMachine, monthlystatsMachine, MissedRevenueMachine, SamplesAssay,
                    UtilizationAssay, RevenueAssay, statsAssay,
                    monthlystatsAssay, MissedRevenueAssay, Csv])
