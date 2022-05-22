import pandas as pd
import numpy as np


assay_list = ["Beta Thalassemia",
         "SickleCellAnemia",
         "Isocitrate Dehydrogenase 1 (Soluble)",
         "Isocitrate Dehydrogenase 2 (Mitochondrial)",
         "DNA Cytosine -5-Methyltransferose 3 Alpha",
         "c-Kit mutation testing",
         "WilmsTumor",
         "C/Enhancer BindingProteinAlpha",
         "IGHV",
         "JAK2 Mutation",
         "Multiple Endocrine Neoplasia Type 2A and 2B",
         "B-raf Gene Mutation",
         "Familial Adinomatous Polyposis",
         "BCR-ABL Kinase Domain Mutation",
         "Chimeric Post-Transplant",
         "Maternal Cells Engraftment - Granulocyte and lymphocyte",
         "Maternal Cells Engraftment - Mother",
         "Chimeric StudyPre-Transplant Recipient",
         "Chimeric StudyDonor",
         "MS-Like Tyrosine Kinase 3",
         "Nucleophosmin Nucleolar Phosphoprotein B23",
         "T-Cell Receptor Gamma Rearrangement",
         "Ig Heav y Chain Rearrangement",
         "BCR-ABL Quantitation",
         "BCR-ABL Subtyping",
         "PML-RAR-alpha t(15;17) Quantitative PCR",
         "RUNX1/ETO",
         "Factor V Leiden Mutation",
         "Prothrombin20210Mutation",
         "MTHFR Deficiency",
         "HeriditaryHemochromatosis",
         "BRCA 1/2 by NGS",
         "Myeloied panel by NGS",
         "BCR-ABL IS",
         "KRAS",
         "NRAS-BRAF",
         "EGFR",
         "B-RAF",
         "DNA Extraction",
         "RNA Extraction",
         "Beta Thalassemia",
         "SickleCellAnemia",
         "Isocitrate Dehydrogenase 1, Soluble",
         "Isocitrate Dehydrogenase 2, Mitochondrial",
         "DNA Cytosine -5-Methyltransferose 3 Alpha",
         "c-Kit mutation testing",
         "WilmsTumor",
         "C/Enhancer BindingProteinAlpha",
         "IGHV",
         "JAK2 Mutation Comprehensive",
         "Multiple Endocrine Neoplasia Type 2A and 2B",
         "B-raf Gene Mutation",
         "Familial Adinomatous",
         "BCR-ABL Kinase Domain Mutation -1st Round",
         "BCR-ABL Kinase Domain Mutation- Nested PCR",
         "Chimeric Post-Transplant",
         "Maternal Cells Engraftment - Granulocyte and lymphocyte",
         "Maternal Cells Engraftment - Mother",
         "Chimeric StudyPre-Transplant Recipient",
         "Chimeric StudyDonor",
         "MS-Like Tyrosine Kinase 3",
         "Nucleophosmin Nucleolar Phosphoprotein B23",
         "T-Cell Receptor Gamma Rearrangement",
         "Ig Heav y Chain Rearrangement",
         "RNA Myeloid panel by NGS",
         "Beta Thalassemia",
         "SickleCellAnemia",
         "Isocitrate Dehydrogenase 1, Soluble",
         "Isocitrate Dehydrogenase 2, Mitochondrial",
         "DNA Cytosine -5-Methyltransferose 3 Alpha",
         "c-Kit mutation testing",
         "WilmsTumor",
         "C/Enhancer BindingProteinAlpha",
         "IGHV",
         "JAK2 Mutation Comprehensive",
         "Multiple Endocrine Neoplasia Type 2A and 2B",
         "B-raf Gene Mutation",
         "Familial Adinomatous Polyposis",
         "BCR-ABL Kinase Domain Mutation",
         "BRCA 1/2 by NGS",
         "Myeloied panel by NGS",
         "BRCA 1/2 by NGS",
         "Myeloied panel by NGS", ]

machines = ["3730xL DNA Analyzer"]*14 + ["3500xL Genetic Analyzer"]*9 + ["Quant studio 6 flex"]*10 + ["GeneXpert"] + ["Idylla"]*4 + \
    ["MagnaPure 96"]*2 + ["Thermocycler ABI Veriti 96 Well Termal System"] * \
    25 + ["Biomek"]*14 + ["Ion chef System"]*2 + ["Ion GeneStudio 5S System"]*2

runtime = [1]*14 + [0.41]*9 + [1.1]*4 + [2]*5 + [0.41] + [1.91] + [2.1, 1.86, 2.5, 1.66] + [1.75]*2 + [1.1]*2 + [1.6]*5 + \
    [2.91]*2 + [2.16, 1.41, 2.5, 1.6, 4.16, 2.28] + [2.83]*5 + \
    [2.4, 1.6, 2.28, 2.28, 0.41] + [0.5]*14 + [7.2, 8] + [8]*2

id_list = ['1_21',
           '2_21',
           '3_21',
           '4_21',
           '5_21',
           '6_21',
           '7_21',
           '8_21',
           '9_21',
           '10_21',
           '11_21',
           '12_21',
           '13_21',
           '14_21',
           '15_21',
           '16_21',
           '17_21',
           '18_21',
           '19_21',
           '20_21',
           '21_21',
           '22_21',
           '23_21',
           '24_21',
           '25_21',
           '26_21',
           '27_21',
           '28_21',
           '29_21',
           '30_21',
           '31_21',
           '32_21',
           '33_21',
           '34_21',
           '35_21',
           '36_21',
           '37_21',
           '38_21',
           '39_21',
           '40_21',
           '41_21',
           '42_21',
           '43_21',
           '44_21',
           '45_21',
           '46_21',
           '47_21',
           '48_21',
           '49_21',
           '50_21',
           '51_21',
           '52_21',
           '53_21',
           '54_21',
           '55_21',
           '56_21',
           '57_21',
           '58_21',
           '59_21',
           '60_21',
           '61_21',
           '62_21',
           '63_21',
           '64_21',
           '65_21',
           '66_21',
           '67_21',
           '68_21',
           '69_21',
           '70_21',
           '71_21',
           '72_21',
           '73_21',
           '74_21',
           '75_21',
           '76_21',
           '77_21',
           '78_21',
           '79_21',
           '80_21',
           '81_21',
           '82_21',
           '83_21']

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
        # TODO: price
        "Price": [100]*len(assay_list),
        # "Maintenance": [520, 520, 520, 520, 520, 520],
        "Run time": runtime,
        "Full capacity": [2000]*len(assay_list),
        "MachineID": id_list,
        "AssayID": id_list,
    })

    records = df_stats.to_dict('records')
    return records


def calculate_revenue(df_year_dict, stats_dict):
    df_year = pd.DataFrame(df_year_dict)
    df_year.index = df_year['AssayID']
    df_year.drop(['AssayID'], inplace=True, axis=1)

    df_stats = pd.DataFrame(stats_dict)

    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (
        df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    df_revenue = pd.DataFrame(df_only_sample.values*(df_stats.Price.values).reshape(
        len(df_only_sample), 1), columns=df_only_sample.columns, index=df_only_sample.index)
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

    df_only_sample = df_year.loc[:, ~((df_year.columns == 'Assay') | (
        df_year.columns == 'Year') | (df_year.columns == 'MachineID'))]
    runtime = (df_stats['Run time'].values).reshape(
        len(df_only_sample), 1) / np.full(shape=(len(df_only_sample), 1), fill_value=60)
    formula = ((df_only_sample.values * runtime))

    df_util = pd.DataFrame(
        formula, columns=df_only_sample.columns, index=df_only_sample.index)
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

    fullcap = (df_stats['Full capacity'].values).reshape(len(df_stats), 1) / np.full(
        shape=(len(df_stats), 1), fill_value=12)  # - df_stats["Maintenance"].values.reshape(6, 1))

    runtime = (df_stats['Run time'].values).reshape(
        len(df_stats), 1) / np.full(shape=(len(df_stats), 1), fill_value=60)

    price = (df_stats['Price'].values).reshape(len(df_stats), 1)

    fullcap_samples = fullcap / runtime

    fullrev = fullcap_samples * price

    df_fullcap = pd.DataFrame(fullcap, columns=['MaxMonthlyhours'])
    df_fullcap['MaxMonthlySamples'] = fullcap_samples
    df_fullcap['MaxMonthlyRevenue'] = fullrev
    df_fullcap['AssayID'] = normalize_index(df_year['AssayID'])
    df_fullcap['MachineID'] = df_year['MachineID']

    records = df_fullcap.to_dict('records')

    return records


def calculate_missedrevenue(df_revenue_dict, stats_dict):
    df_revenue = pd.DataFrame(df_revenue_dict)
    df_stats = pd.DataFrame(stats_dict)

    df_only_revenue = df_revenue.loc[:, ~((df_revenue.columns == 'Assay') | (df_revenue.columns == 'Year') | (
        df_revenue.columns == 'AssayID') | (df_revenue.columns == 'MachineID'))]

    actual_revenue = df_only_revenue.values

    fullcap = (df_stats['Full capacity'].values).reshape(
        len(df_stats), 1) / np.full(shape=(len(df_stats), 1), fill_value=12)
    fullcap = (np.repeat(fullcap[:, :, np.newaxis],
               12, axis=2)).reshape(len(df_stats), 12)

    runtime = (df_stats['Run time'].values).reshape(
        len(df_stats), 1) / np.full(shape=(len(df_stats), 1), fill_value=60)
    runtime = (np.repeat(runtime[:, :, np.newaxis],
               12, axis=2)).reshape(len(df_stats), 12)

    price = (df_stats['Price'].values).reshape(len(df_stats), 1)
    price = (np.repeat(price[:, :, np.newaxis], 12,
             axis=2)).reshape(len(df_stats), 12)

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
