
# coding: utf-8

# In[68]:

import pandas as pd
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv('U.S._Chronic_Disease_Indicators__CDI_.csv')
CancerData = data[data.Topic == 'Cancer']
#separated by region
SeCancer = CancerData[CancerData.LocationAbbr.isin(['NC', 'GA', 'FL', 'MD', 'SC', 'VA', 'WA', 'DC', 'DE', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'])]
NeCancer = CancerData[CancerData.LocationAbbr.isin(['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NY', 'NJ', 'PA'])]
MwCancer = CancerData[CancerData.LocationAbbr.isin(['IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'])]
WCancer = CancerData[CancerData.LocationAbbr.isin(['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA'])]

SeInvasiveCancer = SeCancer[(SeCancer.Question == 'Invasive cancer (all sites combined), mortality') & (SeCancer.StratificationCategory1 == 'Overall') & (SeCancer.DataValueType == 'Average Annual Crude Rate')]
NeInvasiveCancer = NeCancer[(NeCancer.Question == 'Invasive cancer (all sites combined), mortality') & (NeCancer.StratificationCategory1 == 'Overall') & (NeCancer.DataValueType == 'Average Annual Crude Rate')]
MwInvasiveCancer = MwCancer[(MwCancer.Question == 'Invasive cancer (all sites combined), mortality') & (MwCancer.StratificationCategory1 == 'Overall') & (MwCancer.DataValueType == 'Average Annual Crude Rate')]
WInvasiveCancer = WCancer[(WCancer.Question == 'Invasive cancer (all sites combined), mortality') & (WCancer.StratificationCategory1 == 'Overall') & (WCancer.DataValueType == 'Average Annual Crude Rate')]
InvasiveCancer = CancerData[(CancerData.Question == 'Invasive cancer (all sites combined), mortality') & (CancerData.StratificationCategory1 == 'Overall') & (CancerData.DataValueType == 'Average Annual Crude Rate')]

#SeInvasiveCancer.boxplot(column='DataValueAlt')
#NeInvasiveCancer.boxplot(column='DataValueAlt')
#MwInvasiveCancer.boxplot(column='DataValueAlt')
#WInvasiveCancer.boxplot(column='DataValueAlt')
#InvasiveCancer.boxplot(column= 'DataValueAlt')

#Percentage of women aged 50-74 years who use Mammographies

SeMamm = SeCancer[(SeCancer.Question == 'Mammography use among women aged 50-74 years') & (SeCancer.StratificationCategory1 == 'Overall') & (SeCancer.DataValueType == 'Crude Prevalence')]
NeMamm = NeCancer[(NeCancer.Question == 'Mammography use among women aged 50-74 years') & (NeCancer.StratificationCategory1 == 'Overall') & (NeCancer.DataValueType == 'Crude Prevalence')]
MwMamm = MwCancer[(MwCancer.Question == 'Mammography use among women aged 50-74 years') & (MwCancer.StratificationCategory1 == 'Overall') & (MwCancer.DataValueType == 'Crude Prevalence')]
WMamm = WCancer[(WCancer.Question == 'Mammography use among women aged 50-74 years') & (WCancer.StratificationCategory1 == 'Overall') & (WCancer.DataValueType == 'Crude Prevalence')]
USAMamm = CancerData[(CancerData.Question == 'Mammography use among women aged 50-74 years') & (CancerData.StratificationCategory1 == 'Overall') & (CancerData.DataValueType == 'Crude Prevalence')]

avgMammSe = SeMamm['DataValueAlt'].mean() 
avgMammNe = NeMamm['DataValueAlt'].mean()
avgMammMw = MwMamm['DataValueAlt'].mean()
avgMammW = WMamm['DataValueAlt'].mean()
avgUSAMamm = USAMamm['DataValueAlt'].mean()

#USAMamm.boxplot(column='DataValueAlt')
#SeMamm.boxplot(column='DataValueAlt')
#MwMamm.boxplot(column='DataValueAlt')
#WMamm.boxplot(column='DataValueAlt')

SeMammRace = SeCancer[(SeCancer.Question == 'Mammography use among women aged 50-74 years') & (SeCancer.StratificationCategory1 == 'Race/Ethnicity') & (SeCancer.DataValueType == 'Crude Prevalence')]
SeMammBlack = SeMammRace[(SeMammRace.Stratification1 == 'Black, non-Hispanic')]
SeMammHispanic = SeMammRace[(SeMammRace.Stratification1 == 'Hispanic')]
SeMammWhite = SeMammRace[(SeMammRace.Stratification1 == 'White, non-Hispanic')]
SeMammMulti = SeMammRace[(SeMammRace.Stratification1 == 'Multiracial, non-Hispanic')]
SeMammOther = SeMammRace[(SeMammRace.Stratification1 == 'Other, non-Hispanic')]

#SeMammBlack.boxplot(column='DataValueAlt')
#SeMammHispanic.boxplot(column='DataValueAlt')
#SeMammWhite.boxplot(column='DataValueAlt')
#SeMammMulti.boxplot(column='DataValueAlt')
#SeMammOther.boxplot(column= 'DataValueAlt')

stats.ttest_ind(SeMammBlack['DataValueAlt'].dropna(), SeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(SeMammHispanic['DataValueAlt'].dropna(), SeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(SeMammMulti['DataValueAlt'].dropna(), SeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(SeMammOther['DataValueAlt'].dropna(), SeMammWhite['DataValueAlt'].dropna())

NeMammRace = NeCancer[(NeCancer.Question == 'Mammography use among women aged 50-74 years') & (NeCancer.StratificationCategory1 == 'Race/Ethnicity') & (NeCancer.DataValueType == 'Crude Prevalence')]
NeMammBlack = NeMammRace[(NeMammRace.Stratification1 == 'Black, non-Hispanic')]
NeMammHispanic = NeMammRace[(NeMammRace.Stratification1 == 'Hispanic')]
NeMammWhite = NeMammRace[(NeMammRace.Stratification1 == 'White, non-Hispanic')]
NeMammMulti = NeMammRace[(NeMammRace.Stratification1 == 'Multiracial, non-Hispanic')]
NeMammOther = NeMammRace[(NeMammRace.Stratification1 == 'Other, non-Hispanic')]

#NeMammBlack.boxplot(column = 'DataValueAlt')
#NeMammHispanic.boxplot(column = 'DataValueAlt')
#NeMammWhite.boxplot(column = 'DataValueAlt')
#NeMammMulti.boxplot(column = 'DataValueAlt')
#NeMammOther.boxplot(column = 'DataValueAlt')

stats.ttest_ind(NeMammBlack['DataValueAlt'].dropna(), NeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(NeMammHispanic['DataValueAlt'].dropna(), NeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(NeMammMulti['DataValueAlt'].dropna(), NeMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(NeMammOther['DataValueAlt'].dropna(), NeMammWhite['DataValueAlt'].dropna())

MwMammRace = MwCancer[(MwCancer.Question == 'Mammography use among women aged 50-74 years') & (MwCancer.StratificationCategory1 == 'Race/Ethnicity') & (MwCancer.DataValueType == 'Crude Prevalence')]
MwMammBlack = MwMammRace[(MwMammRace.Stratification1 == 'Black, non-Hispanic')]
MwMammHispanic = MwMammRace[(MwMammRace.Stratification1 == 'Hispanic')]
MwMammWhite = MwMammRace[(MwMammRace.Stratification1 == 'White, non-Hispanic')]
MwMammMulti = MwMammRace[(MwMammRace.Stratification1 == 'Multiracial, non-Hispanic')]
MwMammOther = MwMammRace[(MwMammRace.Stratification1 == 'Other, non-Hispanic')]

#MwMammBlack.boxplot(column='DataValueAlt')
#MwMammHispanic.boxplot(column='DataValueAlt')
#MwMammWhite.boxplot(column='DataValueAlt')
#MwMammMulti.boxplot(column='DataValueAlt')
#MwMammOther.boxplot(column= 'DataValueAlt')

stats.ttest_ind(MwMammBlack['DataValueAlt'].dropna(), MwMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(MwMammHispanic['DataValueAlt'].dropna(), MwMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(MwMammMulti['DataValueAlt'].dropna(), MwMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(MwMammOther['DataValueAlt'].dropna(), MwMammWhite['DataValueAlt'].dropna())

WMammRace = WCancer[(WCancer.Question == 'Mammography use among women aged 50-74 years') & (WCancer.StratificationCategory1 == 'Race/Ethnicity') & (WCancer.DataValueType == 'Crude Prevalence')]
WMammBlack = WMammRace[(WMammRace.Stratification1 == 'Black, non-Hispanic')]
WMammHispanic = WMammRace[(WMammRace.Stratification1 == 'Hispanic')]
WMammWhite = WMammRace[(WMammRace.Stratification1 == 'White, non-Hispanic')]
WMammMulti = WMammRace[(WMammRace.Stratification1 == 'Multiracial, non-Hispanic')]
WMammOther = WMammRace[(WMammRace.Stratification1 == 'Other, non-Hispanic')]

#WMammBlack.boxplot(column='DataValueAlt')
#WMammHispanic.boxplot(column='DataValueAlt')
#WMammWhite.boxplot(column='DataValueAlt')
#WMammMulti.boxplot(column='DataValueAlt')
#WMammOther.boxplot(column= 'DataValueAlt')

stats.ttest_ind(WMammBlack['DataValueAlt'].dropna(), WMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(WMammHispanic['DataValueAlt'].dropna(), WMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(WMammMulti['DataValueAlt'].dropna(), WMammWhite['DataValueAlt'].dropna())
stats.ttest_ind(WMammOther['DataValueAlt'].dropna(), WMammWhite['DataValueAlt'].dropna())


