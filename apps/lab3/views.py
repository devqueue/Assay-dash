from .processing import create_df, create_stats, calculate_revenue, calculate_utilization, get_fullcapacity, calculate_missedrevenue
from .forms import CsvModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
from .models import MissedRevenueMachine, UtilizationMachine, SamplesMachine, RevenueMachine, monthlystatsMachine, statsMachine, SamplesAssay, UtilizationAssay, RevenueAssay, MissedRevenueAssay, monthlystatsAssay, statsAssay

from .serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, monthlystatsSerializer, AssayUtilizationSerializer, AssaySamplesSerializer, AssayRevenueSerializer, AssaymonthlystatsSerializer
from .viewfuncs import index_context, sample_context, util_context, revenue_context
import traceback
# Create your views here.


def indexpage(request):
    context = {
        'segment': 'lab3-index',
    }
    samples_obj = SamplesMachine.objects.all()
    revenue_obj = SamplesMachine.objects.all()
    samples_serializer = SamplesSerializer(samples_obj, many=True)
    revenue_serializer = RevenueSerializer(revenue_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    revenue_df = pd.DataFrame(revenue_serializer.data)

    if not samples_df.empty:
        years = samples_df['Year'].unique()
        machines = samples_df['MachineID'].unique()
        months = [col for col in samples_df.columns if col not in (
            'AssayID', 'Assay', 'Year', 'MachineID')]

    if request.method == 'POST':

        YEAR = request.POST['year']
        MONTH = request.POST['month']
        MACHINE = request.POST['assay']

        context |= index_context(YEAR, MONTH, MACHINE, samples_df, revenue_df)
        return render(request, 'labs/index.html', context)

    else:
        if samples_df.empty:
            return render(request, 'labs/index.html', context)

        else:
            YEAR = years[0]
            MONTH = months[0]
            MACHINE = machines[0]
            context |= index_context(
                YEAR, MONTH, MACHINE, samples_df, revenue_df)
            return render(request, 'labs/index.html', context)


def sample(request):
    context = {
        'segment': 'lab3-samples',
    }
    samples_assay_obj = SamplesAssay.objects.all()

    samples_assay_serializer = AssaySamplesSerializer(samples_assay_obj, many=True)

    # Assay dataframes
    samples_assay_df = pd.DataFrame(samples_assay_serializer.data)

    samples_machine_obj = SamplesMachine.objects.all()
    monthlystats_machine_obj = monthlystatsMachine.objects.all()

    samples_serializer = SamplesSerializer(samples_machine_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(
        monthlystats_machine_obj, many=True)

    # machine dataframes
    samples_df = pd.DataFrame(samples_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if not samples_df.empty:
        years = samples_df['Year'].unique()
        months = [col for col in samples_df.columns if col not in (
            'AssayID', 'Assay', 'Year', 'MachineID')]
        machines = samples_df['MachineID'].unique()


        # print(samples_assay_df.column
    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']
        YEAR3 = request.POST['year3']
        MACHINE3 = request.POST['assay3']
        MONTH3 = request.POST['month3']

        context |= sample_context(
            YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE3, MONTH3, samples_df, monthlystats_df, samples_assay_df)
        return render(request, 'labs/sample_lab3.html', context)
    else:
        if samples_df.empty:
            return render(request, 'labs/sample_lab3.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]
            YEAR3 = years[0]
            MACHINE3 = machines[0]
            MONTH3 = months[0]
            context |= sample_context(
                YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE3, MONTH3, samples_df, monthlystats_df, samples_assay_df)

            return render(request, 'labs/sample_lab3.html', context)


def util(request):
    context = {
        'segment': 'lab3-util',
    }

    util_assay_obj = UtilizationAssay.objects.all()

    util_assay_serializer = AssaySamplesSerializer(
        util_assay_obj, many=True)

    # Assay dataframes
    util_assay_df = pd.DataFrame(util_assay_serializer.data)


    util_obj = UtilizationMachine.objects.all()
    monthlystats_obj = monthlystatsMachine.objects.all()

    util_serializer = UtilizationSerializer(util_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(
        monthlystats_obj, many=True)

    util_df = pd.DataFrame(util_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if not util_df.empty:
        years = util_df['Year'].unique()
        months = [col for col in util_df.columns if col not in (
            'AssayID', 'Assay', 'Year', 'MachineID')]
        machines = util_df['MachineID'].unique()

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']
        YEAR3 = request.POST['year3']
        MACHINE2 = request.POST['assay3']
        MONTH3 = request.POST['month3']

        context |= util_context(
            YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE2, MONTH3, util_df, monthlystats_df, util_assay_df)

        return render(request, 'labs/utilization_lab3.html', context)
    else:
        if util_df.empty:
            return render(request, 'labs/utilization_lab3.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]
            YEAR3 = years[0]
            MACHINE2 = machines[0]
            MONTH3 = months[0]

            context |= util_context(
                YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE2, MONTH3, util_df, monthlystats_df, util_assay_df)

            return render(request, 'labs/utilization_lab3.html', context)


def revenue(request):
    context = {
        'segment': 'lab3-revenue',
    }
    
    revenue_assay_obj = RevenueAssay.objects.all()

    revenue_assay_serializer = AssaySamplesSerializer(
        revenue_assay_obj, many=True)

    # Assay dataframes
    revenue_assay_df = pd.DataFrame(revenue_assay_serializer.data)


    revenue_obj = RevenueMachine.objects.all()
    monthlystats_obj = monthlystatsMachine.objects.all()

    revenue_serializer = RevenueSerializer(revenue_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(
        monthlystats_obj, many=True)

    revenue_df = pd.DataFrame(revenue_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if not revenue_df.empty:
        years = revenue_df['Year'].unique()
        months = [col for col in revenue_df.columns if col not in (
            'AssayID', 'Assay', 'Year', 'MachineID')]
        machines = revenue_df['MachineID'].unique()

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']
        YEAR3 = request.POST['year3']
        MACHINE3 = request.POST['assay3']
        MONTH3 = request.POST['month3']

        context |= revenue_context(
            YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE3, MONTH3, revenue_df, monthlystats_df, revenue_assay_df)

        return render(request, 'labs/revenue_lab3.html', context)
    else:
        if revenue_df.empty:
            return render(request, 'labs/revenue_lab3.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]
            YEAR3 = years[0]
            MACHINE3 = machines[0]
            MONTH3 = months[0]

            context |= revenue_context(
                YEAR, MONTH, YEAR2, MACHINE, YEAR3, MACHINE3, MONTH3, revenue_df, monthlystats_df, revenue_assay_df)

            return render(request, 'labs/revenue_lab3.html', context)


@login_required(login_url='/login')
def upload_file(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    context = {
        'segment': 'lab3-upload',
        'form': form
    }

    if form.is_valid():
        context['post'] = True
        file_name = form.cleaned_data.get('file_name')
        file_path = form.cleaned_data.get('file_name').temporary_file_path()

        # Processing CSV FILES

        # Populate the stats
        try:
            df_assay_stats, df_machine_stats  = create_stats()

            Assay_stats_instances = [statsAssay(
                AssayID=rec['AssayID'],
                # MachineID=rec['MachineID'],
                Maintenance=rec['Maintenance'],
                FullCapacity=rec['Full capacity'],
                RunTime=rec['Run time'],
                Price=rec['Price']
            ) for rec in df_assay_stats]

            Machine_stats_instances = [statsMachine(
                # AssayID=rec['AssayID'],
                MachineID=rec['MachineID'],
                Maintenance=rec['Maintenance'],
                FullCapacity=rec['Full capacity'],
                RunTime=rec['Run time'],
                Price=rec['Price']
            ) for rec in df_machine_stats]


            # print(pd.DataFrame(df_machine_stats))
            for row_assay in Assay_stats_instances:
                row_assay.save()

            for row_machine in Machine_stats_instances:
                row_machine.save()
                
            
            # Populate the samples
            df_sample_assay, df_sample_machine = create_df(file_path)

            assay_sample_instances = [SamplesAssay(
                AssayID=record['AssayID'],
                Assay=record['Assay'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_sample_assay]

            Machine_sample_instances = [SamplesMachine(
                MachineID=record['MachineID'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_sample_machine]


            for row_assay in assay_sample_instances:
                row_assay.save()


            for row_machine in Machine_sample_instances:
                row_machine.save()
                

            # Populate the revenue
            df_revenue_assay, df_revenue_machine = calculate_revenue(
                df_sample_assay, df_sample_machine, df_assay_stats, df_machine_stats)
            
            Revenue_Assay = [RevenueAssay(
                AssayID=record['AssayID'],
                Assay=record['Assay'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_revenue_assay]
            

            Revenue_machine = [RevenueMachine(
                MachineID=record['MachineID'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_revenue_machine]

            for row_assay in Revenue_Assay:
                row_assay.save()


            for row_machine in Revenue_machine:
                row_machine.save()

            # Populate the utilization
            df_util_assay, df_util_machine = calculate_utilization(
                df_sample_assay, df_sample_machine, df_assay_stats, df_machine_stats)

            Util_Assay = [UtilizationAssay(
                AssayID=record['AssayID'],
                Assay=record['Assay'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_util_assay]
            
            util_machine = [UtilizationMachine(
                MachineID=record['MachineID'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_util_machine]


            for row_assay in Util_Assay:
                row_assay.save()

            for row_machine in util_machine:
                row_machine.save()



            # Populate the monthly stats
            monthly_stats_assay, monthly_stats_machine = get_fullcapacity(df_assay_stats, df_machine_stats)

            stats_assay = [monthlystatsAssay(
                AssayID=rec['AssayID'],
                MaxMonthlyhours=rec['MaxMonthlyhours'],
                MaxMonthlyRevenue=rec['MaxMonthlyRevenue'],
                MaxMonthSamples=rec['MaxMonthlySamples']
            ) for rec in monthly_stats_assay]

            stats_machine = [monthlystatsMachine(
                MachineID=rec['MachineID'],
                MaxMonthlyhours=rec['MaxMonthlyhours'],
                MaxMonthlyRevenue=rec['MaxMonthlyRevenue'],
                MaxMonthSamples=rec['MaxMonthlySamples']
            ) for rec in monthly_stats_machine]

            for row_assay in stats_assay:
                row_assay.save()

            for row_machine in stats_machine:
                row_machine.save()


            # Populate the missed revenue
            df_missed_assay, df_Missed_machine = calculate_missedrevenue(
                df_revenue_assay, df_revenue_machine, df_assay_stats, df_machine_stats)

            Missed_Assay = [MissedRevenueAssay(
                AssayID=record['AssayID'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_missed_assay]

            Missed_machine = [MissedRevenueMachine(
                MachineID=record['MachineID'],
                January=record['January'],
                February=record['February'],
                March=record['March'],
                April=record['April'],
                May=record['May'],
                June=record['June'],
                July=record['July'],
                August=record['August'],
                September=record['September'],
                October=record['October'],
                November=record['November'],
                December=record['December'],
                Year=record['Year']
            ) for record in df_Missed_machine]

            for row_assay in Missed_Assay:
                row_assay.save()

            for row_machine in Missed_machine:
                row_machine.save()

            context['icon'] = 'success'
            context['Title'] = 'Success'
            context['Text'] = 'Your file has been uploaded sucessfully'
            form.cleaned_data['activated'] = True
            form.save()
        except Exception:
            context['icon'] = 'error'
            context['Title'] = 'Error'
            context['Text'] = "Invalid file data. An error occured, please upload again"
            traceback.print_exc()

    return render(request, 'labs/upload.html', context)
