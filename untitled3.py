# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 07:35:09 2023

@author: HP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stat as sp


df_1 = pd.read_excel("ruralpopolation(total).xlsx")
df_2 = pd.read_excel("urbanpopulation(total).xlsx")
df_3 = pd.read_excel("Accesstoelectricity(rural).xlsx")
df_4 = pd.read_excel("Accesstoelectricity(urban).xlsx")
df_5 = pd.read_excel("co2emissionfrom(liquid).xlsx")
df_6 = pd.read_excel("co2emissionfrom(solid).xlsx")
df_7 = pd.read_excel("all indicatorsnin one file.xlsx")
df_8 = pd.read_excel("Brazil all indicators.xlsx")

'''Creating function'''


#print the title
print(df_1.describe())
print(df_1.median())
kur = pd.DataFrame(sp.kurtosis(df_1))



def filename(file):
    data_O = file
    data_T = file.transpose()
    return data_O, data_T

data_O_1, data_T_1 = filename(df_1)
print(data_O_1.head())
print(data_T_1.head())

data_O_2, data_T_2 = filename(df_2)
print(data_O_2.head())
print(data_T_2.head())

data_O_3, data_T_3 = filename(df_3)
print(data_O_3.head())
print(data_T_3.head())

data_O_4, data_T_4 = filename(df_4)
print(data_O_4.head())
print(data_T_4.head())


data_O_5, data_T_5 = filename(df_5)
print(data_O_5.head())
print(data_T_5.head())


data_O_6, data_T_6 = filename(df_6)
print(data_O_6.head())
print(data_T_6.head())


data_O_7, data_T_7 = filename(df_7)
print(data_O_7.head())
print(data_T_7.head())

data_O_8, data_T_8 = filename(df_8)
print(data_O_8.head())
print(data_T_8.head())
'''Defining the statics properties of some inidicators'''

print(df_1.describe())
print(df_1.median())
Kur = pd.DataFrame(sp.kurtosis(df_1),
                   index=df_1.coulmns,columns=[""])
print(kur)
sku = pd.DataFrame(sp.skew(df_1),index=df_1.columns,columns=[""])
print(sku)

'''Creating Bar_graph for some factors comparision'''
#Bar Graph of co2emissionfrom(solid) & co2emissionfrom(Liquid) df_6 & df_5


New_R_6 = data_O_6[["Country Name", 1995,2000,2005,2010,2015]]
Bar_1 = New_R_6.loc[New_R_6["Country Name"] .isin([ 'Brazil','Germany',
                                                     'Canada', 'Australia',
                                                     'India'])]
plt.figure()
Bar_1.plot(x="Country Name", kind ='bar',figsize=(15,8))
plt.title("CO2 emissions from solid fuel consumption (% of total)",fontsize=20)
plt.xlabel("Country Name")
plt.ylabel("Soild fuel Consumption(% total)")
#plt.legend(1995,2000,2005,2010,2015)
plt.xticks(rotation=0)
plt.show()
plt.savefig("Bar_CO2_Solid")

New_R_5 = data_O_5[["Country Name", 1995,2000,2005,2010,2015]]
Bar_2 = New_R_5.loc[New_R_5["Country Name"] .isin([ 'Brazil','Germany',
                                                     'Canada', 'Australia',
                                                     'India'])]
plt.figure()
Bar_2.plot(x="Country Name", kind ='bar',figsize=(15,8))
plt.title("CO2 emissions from liquid fuel consumption (% of total)",
          fontsize=20)
plt.xlabel("Country Name")
plt.ylabel("Liquid fuel Consumption(% total)")
#plt.legend(1995,2000,2005,2010,2015)
plt.xticks(rotation=0)
plt.show()
plt.savefig("Bar_CO2_liquid")

'''Creating line graph for some factor comparision'''

#Line graph of urban_population & rural_population df_1 & df_2

New_R_1 = data_O_1[["Country Name", 1995,2000,2005,2010,2015]]
line_1 = New_R_1.loc[New_R_1["Country Name"] .isin([ 'Brazil','Germany',
                                                     'Canada', 'Argentina',
                                                     'Japan'])]
line_1 = line_1.set_index("Country Name")
line_1.plot(kind = 'line', figsize=(10,6))
plt.title("Rural_Popolation(total)",fontsize=20)
plt.xlabel("Years")
plt.ylabel("rural_popolation(total)")
plt.legend(loc = 'upper left',ncol=5)
plt.margins(x=0)
plt.savefig("line_rural_population")

New_R_2 = data_O_2[["Country Name", 1995,2000,2005,2010,2015]]
line_2 = New_R_2.loc[New_R_2["Country Name"] .isin([ 'Brazil','Germany',
                                                     'Canada', 'Argentina',
                                                     'Japan'])]

line_2 = line_2.set_index("Country Name")
line_2.plot(kind = 'line', figsize=(10,6))
plt.title("Urban_Population(% total)",fontsize=20)
plt.xlabel("Years")
plt.ylabel("urban_population(% total)")
plt.legend(loc = 'upper left',ncol=5)
plt.margins(x=0)
plt.savefig("line_urban_population")


'''Creatig heath map for correalation'''
#print(data_O_7)
new=data_O_7.set_index("Indicator Name")
new= new.drop(columns=["Country Name"])
newT= new.transpose()
print(newT)
print(new)
plt.figure(figsize=(10,5))
sns.heatmap(newT.corr(), annot= True)
plt.title("Argentina",fontsize=20)
plt.show()
plt.savefig("heatmap_Argentina")
#Heat map for Brazil

new_B=data_O_8.set_index("Indicator Name")
new_B= new_B.drop(columns=["Country Name"])
newT_B= new_B.transpose()
print(newT_B)
print(new_B)
plt.figure(figsize=(10,5))
sns.heatmap(newT_B.corr(), annot= True)
        
plt.title("Brazil",fontsize=20)
plt.show()
plt.savefig("heatmap_Brazil")





