#I've created a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15,
#and a 0 if the country's % Renewable value is below the median.

def answer_ten():
    Top15 = answer_one()
    meann = Top15['% Renewable'].median()

    #Top15['HighRenew'] = pd.Series([1 if (Top15['% Renewable'][country] > meann) for country in Top15.index])
    listt = []
    for country in Top15.index:
        if Top15['% Renewable'][country] > meann or Top15['% Renewable'][country] == meann:
            listt.append(1)
        else:
            listt.append(0)



    Top15['HighRenew']  = listt
    return pd.Series(Top15['HighRenew'])
    

answer_ten()
