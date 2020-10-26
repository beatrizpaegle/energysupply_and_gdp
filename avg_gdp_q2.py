#the average GDP over the last 10 years for each country (excluding missing values from this calculation.)

def answer_three():

    Top15 = answer_one()
    means = pd.Series([Top15.loc[country, [str(x) for x in range(2006,2016)]].mean(skipna=None) for country in list(Top15.index)], index = [country for country in list(Top15.index)])
    return means

answer_three()

#How much had the GDP changed over the 10 year span for the country with the 6th largest average GDP

def answer_four():
    Top15 = answer_one()
    largest_6 = answer_three().sort_values(ascending=False)
    country_6 = largest_6.index[5]
    return Top15.loc[country_6]['2015'] - Top15.loc[country_6]['2006']
answer_four()

#The country that has the maximum % Renewable and the percentage.

def answer_six():
    Top15 = answer_one()
    return (Top15['% Renewable'].index[pd.Index(Top15['% Renewable']).get_loc(max(Top15['% Renewable']))], max(Top15['% Renewable']))

answer_six()


