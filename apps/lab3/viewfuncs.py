
from traceback import print_tb


def index_context(YEAR, MONTH, MACHINE, samples_df, revenue_df):
    years = samples_df['Year'].unique()
    machines = samples_df['MachineID'].unique()
    months = [col for col in samples_df.columns if col not in (
        'AssayID', 'Assay', 'Year', 'MachineID')]

    samples_year = samples_df.loc[samples_df['Year'] == int(YEAR)]
    machine_index = samples_year[[MONTH, 'MachineID']]
    monthly_index = samples_year.loc[samples_year['MachineID'] == MACHINE]
    monthly_index = monthly_index.loc[:, ~((monthly_index.columns == 'Assay') | (monthly_index.columns == 'Year') | (
        monthly_index.columns == 'AssayID') | (monthly_index.columns == 'MachineID'))]

    revenue_year = revenue_df.loc[revenue_df['Year'] == int(YEAR)]
    revenue_only = revenue_year.loc[:, ~((revenue_year.columns == 'Assay') | (
        revenue_year.columns == 'Year') | (revenue_year.columns == 'MachineID'))]

    yearly_revenue = revenue_only.sum(axis=1, numeric_only=True)
    revenue_labels = revenue_year['MachineID']
    y = yearly_revenue.values

    context = {
        'years': years,
        'Machines': machines,
        'Months': months,
        'sel_year': YEAR,
        'sel_month': MONTH,
        'sel_machine': MACHINE,
        'machine_index': machine_index[MONTH].to_list(),
        'machine_labels': machine_index['MachineID'].to_list(),
        'monthly_index': monthly_index.values.reshape(12).tolist(),
        'monthly_labels': monthly_index.columns.tolist(),
        'revenue_lables': revenue_labels.to_list(),
        'revenue_values': list(y)
    }
    return context


def sample_context(YEAR, MONTH, YEAR2, MACHINE, samples_df, monthlystats_df):
    years = samples_df['Year'].unique()
    months = [col for col in samples_df.columns if col not in (
        'AssayID', 'Assay', 'Year', 'MachineID')]
    machines = samples_df['MachineID'].unique()

    samples_year = samples_df.loc[samples_df['Year'] == int(YEAR)]
    machine_samples = samples_year[[MONTH, 'MachineID']]
    maxmonthly_samples = monthlystats_df['MaxMonthSamples'].values
    collected_samples = machine_samples[MONTH].values

    missed_samples = maxmonthly_samples - collected_samples

    # graph 2
    samples_df['Total'] = samples_df.drop(
        'Year', axis=1).sum(axis=1, numeric_only=True)
    df_year_group = samples_df.groupby(['MachineID', 'Year'])

    if YEAR2 == 'All':
        query_all = df_year_group.sum().loc[MACHINE]['Total']
        graph2_labels = list(query_all.index)
        graph2_data = list(query_all)
    else:
        # single years (displaying all months and total)
        query = df_year_group.get_group(
            (MACHINE, int(YEAR2))).select_dtypes(include='number')
        query = query.loc[:, ~(query.columns == 'Year')].reset_index(drop=True)
        graph2_labels = query.columns
        graph2_data = query.loc[0].to_list()

    context = {
        'years': years,
        'Months': months,
        'Machines': machines,
        'sel_year': YEAR,
        'sel_month': MONTH,
        'sel_year2': YEAR2,
        'sel_machine': MACHINE,
        'machine_labels': machine_samples['MachineID'].to_list(),
        'collected_samples': collected_samples,
        'missed_samples': missed_samples,
        'graph2_labels': graph2_labels,
        'graph2_data': graph2_data

    }

    return context


def util_context(YEAR, MONTH, YEAR2, MACHINE, util_df, monthlystats_df):
    years = util_df['Year'].unique()
    months = [col for col in util_df.columns if col not in (
        'AssayID', 'Assay', 'Year', 'MachineID')]
    machines = util_df['MachineID'].unique()

    samples_year = util_df.loc[util_df['Year'] == int(YEAR)]
    machine_util = samples_year[[MONTH, 'MachineID']]

    maxmonthly_util = monthlystats_df['MaxMonthlyhours'].values
    actual_utilizition = machine_util[MONTH].values

    missed_util = maxmonthly_util - actual_utilizition

    # graph2
    util_df['Total'] = util_df.drop(
        'Year', axis=1).sum(axis=1, numeric_only=True)
    df_year_group = util_df.groupby(['MachineID', 'Year'])

    if YEAR2 == 'All':
        query_all = df_year_group.sum().loc[MACHINE]['Total']
        graph2_labels = list(query_all.index)
        graph2_data = list(query_all)
    else:
        # single years (displaying all months and total)
        query = df_year_group.get_group(
            (MACHINE, int(YEAR2))).select_dtypes(include='number')
        query = query.loc[:, ~(query.columns == 'Year')].reset_index(drop=True)
        graph2_labels = query.columns
        graph2_data = query.loc[0].to_list()

    context = {
        'years': years,
        'Months': months,
        'Machines': machines,
        'sel_year': YEAR,
        'sel_month': MONTH,
        'sel_year2': YEAR2,
        'sel_machine': MACHINE,
        'machine_labels': machine_util['MachineID'].to_list(),
        'actual_utilization': actual_utilizition,
        'missed_util': missed_util,
        'graph2_labels': graph2_labels,
        'graph2_data': graph2_data

    }
    return context


def revenue_context(YEAR, MONTH, YEAR2, MACHINE, revenue_df, monthlystats_df):
    years = revenue_df['Year'].unique()
    months = [col for col in revenue_df.columns if col not in (
        'AssayID', 'Assay', 'Year', 'MachineID')]
    machines = revenue_df['MachineID'].unique()

    samples_year = revenue_df.loc[revenue_df['Year'] == int(YEAR)]
    machine_revenue = samples_year[[MONTH, 'MachineID']]

    maxmonthly_revenue = monthlystats_df['MaxMonthlyRevenue'].values
    actual_revenue = machine_revenue[MONTH].values

    missed_revenue = maxmonthly_revenue - actual_revenue

    # graph2
    revenue_df['Total'] = revenue_df.drop(
        'Year', axis=1).sum(axis=1, numeric_only=True)
    df_year_group = revenue_df.groupby(['MachineID', 'Year'])

    if YEAR2 == 'All':
        query_all = df_year_group.sum().loc[MACHINE]['Total']
        graph2_labels = list(query_all.index)
        graph2_data = list(query_all)
    else:
        # single years (displaying all months and total)
        query = df_year_group.get_group(
            (MACHINE, int(YEAR2))).select_dtypes(include='number')
        query = query.loc[:, ~(query.columns == 'Year')].reset_index(drop=True)
        graph2_labels = query.columns
        graph2_data = query.loc[0].to_list()

    context = {
        'years': years,
        'Months': months,
        'Machines': machines,
        'sel_year': YEAR,
        'sel_month': MONTH,
        'sel_year2': YEAR2,
        'sel_machine': MACHINE,
        'machine_labels': machine_revenue['MachineID'].to_list(),
        'actual_revenue': actual_revenue,
        'missed_revenue': missed_revenue,
        'graph2_labels': graph2_labels,
        'graph2_data': graph2_data

    }
    return context

import pandas as pd
import numpy as np


def create_df(csvfilepath):
    df = pd.read_csv(csvfilepath)
    df = df.replace(np.nan, 0)
    records = df.to_dict('records')
    return records


def get_yearfromindex(index):
    _, yearsuf = index[0].split('_')
    year = '20' + yearsuf

    return year


def normalize_index(index):
    flat_index = []
    for i in index:
        assay, _ = i.split('_')
        flat_index.append(assay)
    return flat_index


def create_stats():
    df_stats = pd.DataFrame({
    "Price": [125,275,400,500,400,350],
    "Run time": [2, 45, 120, 20, 20, 1],
    "Full capacity": [6240, 6240, 6240, 6240, 6240, 6240],
    "Maintenance": [520, 520, 520, 520, 520, 520],
    "MachineID": ["FI-MSMS", "GC-MS", "Amino acid analyzer", "LC-MSMS-1" ,"LC-MSMS-2" , "Spectrophotometer"],
    "AssayID": ["SICKPANEL", "OA", "AAA", "VLCFA", "MMA", "SERUM"]
    }, index=["SICKPANEL", "OA", "AAA", "VLCFA", "MMA", "SERUM"])

    records = df_stats.to_dict('records')
    return records


def calculate_revenue(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_year.index = df_year['AssayID']
    df_year.drop(['AssayID'], inplace=True, axis=1)

    df_stats = pd.DataFrame(stats_dict)
    
    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    df_revenue = pd.DataFrame(df_only_sample.values*(df_stats.Price.values).reshape(6,1), columns=df_only_sample.columns, index=df_only_sample.index)
    df_revenue.insert(loc=0, column='Assay', value=df_year['Assay'])
    df_revenue['Year'] = df_year['Year']
    df_revenue['AssayID'] = df_year.index
    df_revenue['MachineID'] = df_year['MachineID']

    records = df_revenue.to_dict('records')
    return records



def calculate_utilization(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_year.index = df_year['AssayID']
    df_year.drop(['AssayID'], inplace=True, axis=1)

    df_stats = pd.DataFrame(stats_dict)

    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1), fill_value=60) 
    formula = ((df_only_sample.values * runtime))

    df_util = pd.DataFrame(formula, columns=df_only_sample.columns, index=df_only_sample.index)
    df_util = df_util.round(2)
    df_util.insert(loc=0, column='Assay', value=df_year['Assay'])
    df_util['Year'] = df_year['Year']
    df_util['AssayID'] = df_year.index
    df_util['MachineID'] = df_year['MachineID']

    record = df_util.to_dict('records')
    return record


def get_fullcapacity(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_stats = pd.DataFrame(stats_dict)

    fullcap = ((df_stats['Full capacity'].values).reshape(6,1) - df_stats["Maintenance"].values.reshape(6,1)) / np.full(shape=(6,1),fill_value=12)
    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=60)
    price = (df_stats['Price'].values).reshape(6,1)

    fullcap_samples = fullcap / runtime

    fullrev = fullcap_samples * price

    df_fullcap = pd.DataFrame(fullcap, columns=['MaxMonthlyhours'])
    df_fullcap['MaxMonthlySamples'] = fullcap_samples
    df_fullcap['MaxMonthlyRevenue'] = fullrev
    df_fullcap['AssayID'] = normalize_index(df_year['AssayID'])
    df_fullcap['MachineID'] = df_year['MachineID']

    records  = df_fullcap.to_dict('records')

    return records


def calculate_missedrevenue(df_revenue_dict, stats_dict):
    df_revenue = pd.DataFrame(df_revenue_dict)
    df_stats = pd.DataFrame(stats_dict)

    df_only_revenue = df_revenue.loc[:, ~((df_revenue.columns == 'Assay') | (df_revenue.columns == 'Year') | (df_revenue.columns == 'AssayID') | (df_revenue.columns == 'MachineID') )]

    actual_revenue = df_only_revenue.values

    fullcap = (df_stats['Full capacity'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=12)
    fullcap = (np.repeat(fullcap[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    runtime = (df_stats['Run time'].values).reshape(6,1) / np.full(shape=(6,1),fill_value=60)
    runtime = (np.repeat(runtime[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    price = (df_stats['Price'].values).reshape(6,1)
    price = (np.repeat(price[:, :, np.newaxis], 12, axis=2)).reshape(6, 12)

    fullcap_samples = fullcap / runtime
    full_revenue = fullcap_samples * price

    missedrev = full_revenue - actual_revenue
    
    df_missedrev = pd.DataFrame(missedrev, columns=df_only_revenue.columns)
    df_missedrev['AssayID'] = df_revenue['AssayID']
    df_missedrev['Assay'] = df_revenue['Assay']
    df_missedrev['Year'] = df_revenue['Year']
    df_missedrev['MachineID'] = df_revenue['MachineID']

    record = df_missedrev.to_dict('records')
    return record