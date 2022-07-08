reviews.groupby('points').points.count()   #just like values_count()

reviews.groupby('points').price.min()

reviews.groupby('winery').apply(lambda df: df.title.iloc[0])  #selecting the name of the first wine reviewed from each winery in the dataset

reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])  #pick out the best wine by country and province:

reviews.groupby(['country']).price.agg([len, min, max])

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed

mi = countries_reviewed.index
type(mi)

countries_reviewed.reset_index()

countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

countries_reviewed.sort_values(by='len', ascending=False)

countries_reviewed.sort_index()

countries_reviewed.sort_values(by=['country', 'len'])


