from .processing import create_df, create_stats, calculate_revenue, calculate_utilization, get_fullcapacity, calculate_missedrevenue
from .forms import CsvModelForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pandas as pd
from .models import MissedRevenue, Utilization, Samples, Revenue, monthlystats, stats
from .serializers import UtilizationSerializer, SamplesSerializer, RevenueSerializer, monthlystatsSerializer
from .viewfuncs import index_context, sample_context, util_context, revenue_context
import traceback
# Create your views here.


def indexpage(request):
    context = {
        'segment': 'lab3-index',
    }
    samples_obj = Samples.objects.all()
    revenue_obj = Revenue.objects.all()
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
    samples_obj = Samples.objects.all()
    monthlystats_obj = monthlystats.objects.all()

    samples_serializer = SamplesSerializer(samples_obj, many=True)
    monthlystats_serializer = monthlystatsSerializer(
        monthlystats_obj, many=True)

    samples_df = pd.DataFrame(samples_serializer.data)
    monthlystats_df = pd.DataFrame(monthlystats_serializer.data)

    if not samples_df.empty:
        years = samples_df['Year'].unique()
        months = [col for col in samples_df.columns if col not in (
            'AssayID', 'Assay', 'Year', 'MachineID')]
        machines = samples_df['MachineID'].unique()

    if request.method == 'POST':
        YEAR = request.POST['year']
        MONTH = request.POST['month']
        YEAR2 = request.POST['year2']
        MACHINE = request.POST['assay2']

        context |= sample_context(
            YEAR, MONTH, YEAR2, MACHINE, samples_df, monthlystats_df)
        return render(request, 'labs/sample.html', context)
    else:
        if samples_df.empty:
            return render(request, 'labs/sample.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]
            context |= sample_context(
                YEAR, MONTH, YEAR2, MACHINE, samples_df, monthlystats_df)

            return render(request, 'labs/sample.html', context)


def util(request):
    context = {
        'segment': 'lab3-util',
    }
    util_obj = Utilization.objects.all()
    monthlystats_obj = monthlystats.objects.all()

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

        context |= util_context(
            YEAR, MONTH, YEAR2, MACHINE, util_df, monthlystats_df)

        return render(request, 'labs/utilization.html', context)
    else:
        if util_df.empty:
            return render(request, 'labs/utilization.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]

            context |= util_context(
                YEAR, MONTH, YEAR2, MACHINE, util_df, monthlystats_df)

            return render(request, 'labs/utilization.html', context)


def revenue(request):
    context = {
        'segment': 'lab3-revenue',
    }
    revenue_obj = Revenue.objects.all()
    monthlystats_obj = monthlystats.objects.all()

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

        context |= revenue_context(
            YEAR, MONTH, YEAR2, MACHINE, revenue_df, monthlystats_df)

        return render(request, 'labs/revenue.html', context)
    else:
        if revenue_df.empty:
            return render(request, 'labs/revenue.html', context)
        else:
            YEAR = years[0]
            MONTH = months[0]
            YEAR2 = years[0]
            MACHINE = machines[0]

            context |= revenue_context(
                YEAR, MONTH, YEAR2, MACHINE, revenue_df, monthlystats_df)

            return render(request, 'labs/revenue.html', context)


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

        # form.save()
        # form = CsvModelForm()
        # obj = Csv.objects.get(activated=False)

        # Processing CSV FILES

        # Populate the stats
        try:
            df_stats = create_stats()
            stats_instances = [stats(
                AssayID=rec['AssayID'],
                MachineID=rec['MachineID'],
                # Maintenance=rec['Maintenance'],
                FullCapacity=rec['Full capacity'],
                RunTime=rec['Run time'],
                Price=rec['Price']
            ) for rec in df_stats]
            try:
                stats.objects.bulk_create(stats_instances)
            except Exception:
                traceback.print_exc()
                stats.objects.bulk_update(stats_instances, fields=[
                                          'FullCapacity', 'RunTime', 'Price', 'Maintenance'])

            # Populate the samples
            df_samples = create_df(file_path)
            sample_instances = [Samples(
                AssayID=record['AssayID'],
                MachineID=record['MachineID'],
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
            ) for record in df_samples]

            try:
                Samples.objects.bulk_create(sample_instances)
            except Exception:
                Samples.objects.bulk_update(sample_instances,
                                            fields=['Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                                                    'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
                traceback.print_exc()

            # Populate the revenue
            revenue_dict = calculate_revenue(df_samples, df_stats)
            Revenue_instances = [Revenue(
                AssayID=record['AssayID'],
                MachineID=record['MachineID'],
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
            ) for record in revenue_dict]

            try:
                Revenue.objects.bulk_create(Revenue_instances)
            except Exception:
                Revenue.objects.bulk_update(Revenue_instances,
                                            fields=['Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                                                    'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
                traceback.print_exc()

            # Populate the utilization
            utilization_dict = calculate_utilization(df_samples, df_stats)
            util_instances = [Utilization(
                AssayID=record['AssayID'],
                MachineID=record['MachineID'],
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
            ) for record in utilization_dict]

            try:
                Utilization.objects.bulk_create(util_instances)
            except Exception:
                Utilization.objects.bulk_update(util_instances,
                                                fields=['Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                                                        'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
                traceback.print_exc()

            # Populate the monthly stats
            monthly_stats = get_fullcapacity(df_samples, df_stats)
            mstats_instances = [monthlystats(
                AssayID=rec['AssayID'],
                MachineID=rec['MachineID'],
                MaxMonthlyhours=rec['MaxMonthlyhours'],
                MaxMonthlyRevenue=rec['MaxMonthlyRevenue'],
                MaxMonthSamples=rec['MaxMonthlySamples']
            ) for rec in monthly_stats]

            try:
                monthlystats.objects.bulk_create(mstats_instances)
            except Exception:
                monthlystats.objects.bulk_update(mstats_instances,
                                                 fields=['MaxMonthlyhours', 'MaxMonthlyRevenue', 'MaxMonthSamples'])
                traceback.print_exc()

            # Populate the missed revenue
            missed_dict = calculate_missedrevenue(revenue_dict, df_stats)

            Missed_instances = [MissedRevenue(
                AssayID=record['AssayID'],
                MachineID=record['MachineID'],
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
            ) for record in missed_dict]

            try:
                MissedRevenue.objects.bulk_create(Missed_instances)
            except Exception:
                MissedRevenue.objects.bulk_update(Missed_instances,
                                                  fields=['Assay', 'January', 'February', 'March', 'April', 'May', 'June',
                                                          'July', 'August', 'September', 'October', 'November', 'December', 'Year'])
                traceback.print_exc()

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
