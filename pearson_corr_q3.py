#Creating a new column that is the ratio of Self-Citations to Total Citations. 
#What is the maximum value for this new column, and what country has the highest ratio?

def answer_seven():
    Top15 = answer_one()

    Top15['Ratio'] = Top15['Self-citations']/Top15['Citations']

    return Top15['Ratio'].index[pd.Index(Top15['Ratio']).get_loc(max(Top15['Ratio']))], max(Top15['Ratio'])



#Creating a column that estimates the population using Energy Supply and Energy Supply per capita. 
#What is the third most populous country according to this estimate?

def answer_eight():
    Top15 = answer_one()
    Top15['ratio_pop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']

    return Top15['ratio_pop'].sort_values(ascending=False).index[2]
    
#Creating column that estimates the number of citable documents per person. 
#What is the correlation between the number of citable documents per capita and the energy supply per capita? 
#I've used the .corr() method, (Pearson's correlation).

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
answer_nine()
