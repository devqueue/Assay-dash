import pandas as pd
import numpy as np
from .assayinfo import assay_list, runtime, AssayID, MachineID


def create_df(csvfilepath):
    df_assay = pd.read_csv(csvfilepath)
    df_assay = df_assay.replace(np.nan, 0)

    assay_records = df_assay.to_dict('records')

    df_assay[["MachineID", "ASSAY"]] = df_assay['MachineID'].str.split(
        "--", expand=True)

    df_assay = df_assay.drop(['ASSAY'], axis=1)
    year = df_assay['Year'][0]
    df_assay = df_assay.groupby('MachineID', as_index=False).agg('sum')
    df_assay['Year'] = [year]*len(df_assay)

    machine_records = df_assay.to_dict('records')

    return (assay_records, machine_records)


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
        # TODO: maintainance
        "Price": [1000]*len(assay_list),
        "Maintenance": [0]*len(assay_list),
        "Run time": runtime,
        "Full capacity": [2000]*len(assay_list),
        "MachineID":  MachineID,
        "AssayID": AssayID,
    })

    df_assay_stats = df_stats.to_dict('records')

    df_stats[["MachineID", "ASSAY"]] = df_stats['MachineID'].str.split(
        "--", expand=True)
    df_stats = df_stats.drop(['ASSAY'], axis=1)
    df_stats = df_stats.groupby('MachineID', as_index=False).agg('mean')

    df_machine_stats = df_stats.to_dict('records')
    return (df_assay_stats, df_machine_stats)


def calculate_revenue(df_assay_dict, df_machine_dict, assay_stats, machine_stats):
    df_assay = pd.DataFrame(df_assay_dict)
    df_machine = pd.DataFrame(df_machine_dict)
    df_assay_stats = pd.DataFrame(assay_stats)
    df_machine_stats = pd.DataFrame(machine_stats)

    df_only_sample_assay = df_assay.loc[:, ~((df_assay.columns == 'Assay') |
                                             (df_assay.columns == 'Year') | (df_assay.columns == 'MachineID') | (df_assay.columns == 'AssayID'))]
    df_only_sample_machine = df_machine.loc[:, ~((df_machine.columns == 'Assay') |
                                                 (df_machine.columns == 'Year') | (df_machine.columns == 'MachineID') | (df_machine.columns == 'AssayID'))]
    df_revenue_assay = pd.DataFrame(df_only_sample_assay.values*(df_assay_stats['Price'].values).reshape(len(df_assay_stats), 1),
                                    columns=df_only_sample_assay.columns, index=df_only_sample_assay.index)

    df_revenue_machine = pd.DataFrame(df_only_sample_machine.values*(df_machine_stats['Price'].values).reshape(len(df_machine_stats), 1),
                                      columns=df_only_sample_machine.columns, index=df_only_sample_machine.index)

    df_revenue_assay['Year'] = df_assay['Year']
    df_revenue_assay['AssayID'] = df_assay['AssayID']
    df_revenue_assay['Assay'] = df_assay['Assay']

    df_revenue_machine['Year'] = df_machine['Year']
    df_revenue_machine['MachineID'] = df_machine['MachineID']

    df_assay_revenue = df_revenue_assay.to_dict('records')
    df_machine_revenue = df_revenue_machine.to_dict('records')

    return (df_assay_revenue, df_machine_revenue)


def calculate_utilization(df_assay_dict, df_machine_dict, assay_stats, machine_stats):
    df_assay = pd.DataFrame(df_assay_dict)
    df_machine = pd.DataFrame(df_machine_dict)
    df_assay_stats = pd.DataFrame(assay_stats)
    df_machine_stats = pd.DataFrame(machine_stats)

    df_only_sample_assay = df_assay.loc[:, ~((df_assay.columns == 'Assay') |
                                             (df_assay.columns == 'Year') | (df_assay.columns == 'MachineID') | (df_assay.columns == 'AssayID'))]
    df_only_sample_machine = df_machine.loc[:, ~((df_machine.columns == 'Assay') |
                                                 (df_machine.columns == 'Year') | (df_machine.columns == 'MachineID') | (df_machine.columns == 'AssayID'))]

    runtime_assay = (df_assay_stats['Run time'].values).reshape(
        len(df_assay_stats), 1) / np.full(shape=(len(df_assay_stats), 1), fill_value=60)

    runtime_machine = (df_machine_stats['Run time'].values).reshape(
        len(df_machine_stats), 1) / np.full(shape=(len(df_machine_stats), 1), fill_value=60)

    formula_assay = ((df_only_sample_assay.values * runtime_assay))

    formula_machine = ((df_only_sample_machine.values * runtime_machine))

    df_util_assay = pd.DataFrame(
        formula_assay, columns=df_only_sample_assay.columns, index=df_only_sample_assay.index)

    df_util_machine = pd.DataFrame(
        formula_machine, columns=df_only_sample_machine.columns, index=df_only_sample_machine.index)

    df_util_assay = df_util_assay.round(2)
    df_util_machine = df_util_machine.round(2)

    df_util_assay['Year'] = df_assay['Year']
    df_util_assay['AssayID'] = df_assay['AssayID']
    df_util_assay['Assay'] = df_assay['Assay']

    df_util_machine['Year'] = df_machine['Year']
    df_util_machine['MachineID'] = df_machine['MachineID']

    df_assay_util = df_util_assay.to_dict('records')
    df_machine_util = df_util_machine.to_dict('records')

    return (df_assay_util, df_machine_util)


def get_fullcapacity(assay_stats, machine_stats):

    df_assay_stats = pd.DataFrame(assay_stats)
    df_machine_stats = pd.DataFrame(machine_stats)

    fullcap_assay = (df_assay_stats['Full capacity'].values).reshape(len(df_assay_stats), 1) / np.full(
        shape=(len(df_assay_stats), 1), fill_value=12) - df_assay_stats["Maintenance"].values.reshape(len(df_assay_stats), 1)

    fullcap_machine = (df_machine_stats['Full capacity'].values).reshape(len(df_machine_stats), 1) / np.full(
        shape=(len(df_machine_stats), 1), fill_value=12) - df_machine_stats["Maintenance"].values.reshape(len(df_machine_stats), 1)

    runtime_assay = (df_assay_stats['Run time'].values).reshape(
        len(df_assay_stats), 1) / np.full(shape=(len(df_assay_stats), 1), fill_value=60)

    runtime_machine = (df_machine_stats['Run time'].values).reshape(
        len(df_machine_stats), 1) / np.full(shape=(len(df_machine_stats), 1), fill_value=60)

    price_assay = (df_assay_stats['Price'].values).reshape(
        len(df_assay_stats), 1)

    price_machine = (df_machine_stats['Price'].values).reshape(
        len(df_machine_stats), 1)

    fullcap_samples_assay = fullcap_assay / runtime_assay
    fullcap_samples_machine = fullcap_machine / runtime_machine

    fullrev_assay = fullcap_samples_assay * price_assay
    fullrev_machine = fullcap_samples_machine * price_machine

    df_fullcap_assay = pd.DataFrame(fullcap_assay, columns=['MaxMonthlyhours'])
    df_fullcap_assay['MaxMonthlySamples'] = fullcap_samples_assay
    df_fullcap_assay['MaxMonthlyRevenue'] = fullrev_assay
    df_fullcap_assay['AssayID'] = df_assay_stats['AssayID']

    df_fullcap_machine = pd.DataFrame(
        fullcap_machine, columns=['MaxMonthlyhours'])
    df_fullcap_machine['MaxMonthlySamples'] = fullcap_samples_machine
    df_fullcap_machine['MaxMonthlyRevenue'] = fullrev_machine
    df_fullcap_machine['MachineID'] = df_machine_stats['MachineID']

    df_assay_fullcap = df_fullcap_assay.to_dict('records')
    df_machine_fullcap = df_fullcap_machine.to_dict('records')

    return (df_assay_fullcap, df_machine_fullcap)


def calculate_missedrevenue(df_assayRevenue_dict, df_machineRevenue_dict, assay_stats, machine_stats):
    df_assayRevenue = pd.DataFrame(df_assayRevenue_dict)
    df_machineRevenue = pd.DataFrame(df_machineRevenue_dict)
    df_assay_stats = pd.DataFrame(assay_stats)
    df_machine_stats = pd.DataFrame(machine_stats)

    df_only_assayRevenue = df_assayRevenue.loc[:, ~((df_assayRevenue.columns == 'Assay') | (df_assayRevenue.columns == 'Year') | (
        df_assayRevenue.columns == 'AssayID') | (df_assayRevenue.columns == 'MachineID'))]

    df_only_MachineRevenue = df_machineRevenue.loc[:, ~((df_machineRevenue.columns == 'Assay') | (df_machineRevenue.columns == 'Year') | (
        df_machineRevenue.columns == 'AssayID') | (df_machineRevenue.columns == 'MachineID'))]

    Actual_Assay_Revenue = df_only_assayRevenue.values

    fullcap_assay = (df_assay_stats['Full capacity'].values).reshape(
        len(df_assay_stats), 1) / np.full(shape=(len(df_assay_stats), 1), fill_value=12)

    fullcap_assay = (np.repeat(fullcap_assay[:, :, np.newaxis],
                               12, axis=2)).reshape(len(df_assay_stats), 12)

    runtime_assay = (df_assay_stats['Run time'].values).reshape(
        len(df_assay_stats), 1) / np.full(shape=(len(df_assay_stats), 1), fill_value=60)

    runtime_assay = (np.repeat(runtime_assay[:, :, np.newaxis],
                               12, axis=2)).reshape(len(df_assay_stats), 12)

    price_assay = (df_assay_stats['Price'].values).reshape(
        len(df_assay_stats), 1)

    price_assay = (np.repeat(price_assay[:, :, np.newaxis], 12,
                             axis=2)).reshape(len(df_assay_stats), 12)

    fullcap_samples_assay = fullcap_assay / runtime_assay
    full_revenue_assay = fullcap_samples_assay * price_assay

    missedrev_assay = full_revenue_assay - Actual_Assay_Revenue

    df_missedrev_assay = pd.DataFrame(
        missedrev_assay, columns=df_only_assayRevenue.columns)

    df_missedrev_assay['Year'] = df_assayRevenue['Year']
    df_missedrev_assay['AssayID'] = df_assayRevenue['AssayID']

    Actual_machine_Revenue = df_only_MachineRevenue.values

    fullcap_machine = (df_machine_stats['Full capacity'].values).reshape(
        len(df_machine_stats), 1) / np.full(shape=(len(df_machine_stats), 1), fill_value=12)

    fullcap_machine = (np.repeat(fullcap_machine[:, :, np.newaxis],
                                 12, axis=2)).reshape(len(fullcap_machine), 12)

    runtime_machine = (df_machine_stats['Run time'].values).reshape(
        len(df_machine_stats), 1) / np.full(shape=(len(df_machine_stats), 1), fill_value=60)

    runtime_machine = (np.repeat(runtime_machine[:, :, np.newaxis],
                                 12, axis=2)).reshape(len(runtime_machine), 12)


    price_machine = (df_machine_stats['Price'].values).reshape(
        len(df_machine_stats), 1)

    price_machine = (np.repeat(price_machine[:, :, np.newaxis], 12,
                               axis=2)).reshape(len(price_machine), 12)


    fullcap_samples_machine = fullcap_machine / runtime_machine
    full_revenue_machine = fullcap_samples_machine * price_machine

    missedrev_machine = full_revenue_machine - Actual_machine_Revenue

    df_missedrev_machine = pd.DataFrame(
        missedrev_machine, columns=df_only_MachineRevenue.columns)

    df_missedrev_machine['Year'] = df_machineRevenue['Year']
    df_missedrev_machine['MachineID'] = df_machineRevenue['MachineID']

    df_assay_misssed = df_missedrev_assay.to_dict('records')
    df_machine_misssed = df_missedrev_machine.to_dict('records')
    
    return (df_assay_misssed, df_machine_misssed)
