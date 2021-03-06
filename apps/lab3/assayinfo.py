
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

runtime = [60/96]*14 + [25/24]*9 + [70/96]*4 + [120/96]*5 + [25/12] + [115] + [170, 112, 150, 100] + [105/48]*2 + [126/96]*2 + [100/96]*5 + \
    [175/96]*2 + [130/96, 85/96, 150/96, 100/96, 250/96, 137/96] + [170/96]*5 + \
    [146/96, 100/96, 137/96, 137/96, 25/12] + [30/96]*14 + [432/6, 480/12] + [480/6, 480/12]

AssayID = ["B-Thal--3730xL_21",
           "SC--3730xL_21",
           "IDH1--3730xL_21",
           "IDH2--3730xL_21",
           "DNMT3A--3730xL_21",
           "C-KIT--3730xL_21",
           "WT--3730xL_21",
           "CEBPA--3730xL_21",
           "IGHV--3730xL_21",
           "JAK2--3730xL_21",
           "MEN2--3730xL_21",
           "BRAF--3730xL_21",
           "FAP--3730xL_21",
           "KINASE--3730xL_21",
           "POST--3500xL_21",
           "POST G & L--3500xL_21",
           "MATERNAL--3500xL_21",
           "PRE--3500xL_21",
           "DON--3500xL_21",
           "FLT3--3500xL_21",
           "NPM--3500xL_21",
           "TCR--3500xL_21",
           "IGH--3500xL_21",
           "Quant--QS6Flex_21",
           "Sub--QS6Flex_21",
           "PML--QS6Flex_21",
           "ETO--QS6Flex_21",
           "FVL--QS6Flex_21",
           "PT--QS6Flex_21",
           "MTHFR--QS6Flex_21",
           "HFE--QS6Flex_21",
           "BRCA--QS6Flex_21",
           "Myeloid - -QS6Flex_21",
           "IS--Xpert_21",
           "KRAS--Idylla_21",
           "NRAS-BRAF--Idylla_21",
           "EGFR--Idylla_21",
           "BRAF--Idylla_21",
           "DNA--MP96_21",
           "RNA - -MP96_21",
           "B-Thal--Termo_21",
           "SC--Termo_21",
           "IDH1--Termo_21",
           "IDH2--Termo_21",
           "DNMT3A--Termo_21",
           "C-KIT--Termo_21",
           "WT--Termo_21",
           "CEBPA--Termo_21",
           "IGHV--Termo_21",
           "JAK2--Termo_21",
           "MEN2--Termo_21",
           "BRAF--Termo_21",
           "FAP--Termo_21",
           "Ki-1st-round--Termo_21",
           "Ki-nested-pcr--Termo_21",
           "POST--Termo_21",
           "POST G & L--Termo_21",
           "MATERNAL--Termo_21",
           "PRE--Termo_21",
           "DON--Termo_21",
           "FLT3--Termo_21",
           "NPM--Termo_21",
           "TCR--Termo_21",
           "IGH--Termo_21",
           "RNA Myeloid--Termo_21",
           "B-Thal--Biomek_21",
           "SC--Biomek_21",
           "IDH1--Biomek_21",
           "IDH2--Biomek_21",
           "DNMT3A--Biomek_21",
           "C-KIT--Biomek_21",
           "WT--Biomek_21",
           "CEBPA--Biomek_21",
           "IGHV--Biomek_21",
           "JAK2--Biomek_21",
           "MEN2--Biomek_21",
           "BRAF--Biomek_21",
           "FAP--Biomek_21",
           "KINASE--Biomek_21",
           "BRCA--Ion Chef_21",
           "Myeloid - -Ion Chef_21",
           "BRCA--Ion 5S_21",
           "Myeloid - -Ion 5S_21", ]

MachineID = ["3730xL--B-Thal",
             "3730xL--SC",
             "3730xL--IDH1",
             "3730xL--IDH2",
             "3730xL--DNMT3A",
             "3730xL--C-KIT",
             "3730xL--WT",
             "3730xL--CEBPA",
             "3730xL--IGHV",
             "3730xL--JAK2",
             "3730xL--MEN2",
             "3730xL--BRAF",
             "3730xL--FAP",
             "3730xL--KINASE",
             "3500xL--POST",
             "3500xL--POST G & L",
             "3500xL--MATERNAL",
             "3500xL--PRE",
             "3500xL--DON",
             "3500xL--FLT3",
             "3500xL--NPM",
             "3500xL--TCR",
             "3500xL--IGH",
             "QS6Flex--Quant",
             "QS6Flex--Sub",
             "QS6Flex--PML",
             "QS6Flex--ETO",
             "QS6Flex--FVL",
             "QS6Flex--PT",
             "QS6Flex--MTHFR",
             "QS6Flex--HFE",
             "QS6Flex--BRCA",
             "QS6Flex--Myeloid",
             "Xpert--IS",
             "Idylla--KRAS",
             "Idylla--NRAS-BRAF",
             "Idylla--EGFR",
             "Idylla--BRAF",
             "MP96--DNA",
             "MP96--RNA",
             "Termo--B-Thal",
             "Termo--SC",
             "Termo--IDH1",
             "Termo--IDH2",
             "Termo--DNMT3A",
             "Termo--C-KIT",
             "Termo--WT",
             "Termo--CEBPA",
             "Termo--IGHV",
             "Termo--JAK2",
             "Termo--MEN2",
             "Termo--BRAF",
             "Termo--FAP",
             "Termo--Ki-1st-round",
             "Termo--Ki-nested-pcr",
             "Termo--POST",
             "Termo--POST G & L",
             "Termo--MATERNAL",
             "Termo--PRE",
             "Termo--DON",
             "Termo--FLT3",
             "Termo--NPM",
             "Termo--TCR",
             "Termo--IGH",
             "Termo--RNA Myeloid",
             "Biomek--B-Thal",
             "Biomek--SC",
             "Biomek--IDH1",
             "Biomek--IDH2",
             "Biomek--DNMT3A",
             "Biomek--C-KIT",
             "Biomek--WT",
             "Biomek--CEBPA",
             "Biomek--IGHV",
             "Biomek--JAK2",
             "Biomek--MEN2",
             "Biomek--BRAF",
             "Biomek--FAP",
             "Biomek--KINASE",
             "Ion Chef--BRCA",
             "Ion Chef--Myeloid",
             "Ion 5S--BRCA",
             "Ion 5S--Myeloid", ]
