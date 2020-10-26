
def answer_one():

#The energy data from the file Energy Indicators.xls is a list of indicators of energy supply and renewable electricity production from the United Nations 
#for the year 2013, and will be put into a DataFrame with the variable name of energy. Here I treated and cleaned somethings to make my work easier.
 
    import pandas as pd
    import re
    energy = pd.read_excel(r'Energy Indicators.xls')
    energy = energy.drop(["Unnamed: 0", "Unnamed: 1"], axis=1)
    energy = energy.rename(columns={'Environmental Indicators: Energy': 'Country', 'Unnamed: 3': 'Energy Supply', 'Unnamed: 4': 'Energy Supply per Capita', 'Unnamed: 5':'% Renewable'})
    energy = energy.drop ([x for x in range(16)], axis=0)
    energy = energy.drop ([x for x in range (243, 281)], axis=0)
    energy = energy.reset_index()
    
#There are also several countries with numbers and/or parenthesis in their name. I remove these

    new_list = [re.sub(r'\(.*$', "", s) for s in energy['Country']]
    new_new_list = [re.sub('\d.*',"", d) for d in new_list]

#here I change some country names to facilitate in others codes in this project
    
    new_serie = pd.Series(new_new_list).replace('Iran ', 'Iran')
    energy_ = new_serie.replace({"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"})
    
#here I converted Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule).
    energy['Country'] = energy_
    energy['Energy Supply'] = 1000000*energy['Energy Supply']



#Next, I've loaded the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. 
#I've called this DataFrame GDP. I skipped the header and renamed some countries.
    GDP=pd.read_csv('world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.drop([str(x) for x in range (1960, 2006)], axis = 1)
    GDP = GDP.set_index('Country')
    
#Finally, I've loaded the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, 
#which ranks countries based on their journal contributions in the aforementioned area. I've called this DataFrame ScimEn.
    ScimEn = pd.read_excel(r'scimagojr-3.xlsx')
    ScimEn = ScimEn.drop([x for x in range (15, 191)], axis = 0)
    ScimEn = ScimEn.set_index('Country')

#Here I joined the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
#I used only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
#The index of this DataFrame is the name of the country, 
    merge_1 = pd.merge(GDP, energy, how='outer', left_index=True, right_index=True)
    merge_2 = pd.merge(merge_1, ScimEn, how='inner', left_index=True, right_index=True)
    merge_2 = merge_2.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'index'], axis=1)
    merge_3 = merge_2[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    merge_3['Energy Supply'] = merge_3['Energy Supply'].astype('float64')
    merge_3['Energy Supply per Capita'] = merge_3['Energy Supply per Capita'].astype('float64')
    merge_3['% Renewable'] = merge_3['% Renewable'].astype('float64')
    
    return merge_3
