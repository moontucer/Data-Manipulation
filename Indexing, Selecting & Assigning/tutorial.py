reviews

reviews.country

reviews['country']

reviews['country'][0]

reviews.iloc[0]

reviews.iloc[:, 0]

reviews.iloc[:3, 0] #row first then column second 

reviews.iloc[1:3, 0] # 2 first entries only (3-1) and whole first (0) column

reviews.iloc[[0, 1, 2], 0] #pass a list

reviews.iloc[-5:]

reviews.loc[0, 'country'] #awl value f (0,0)

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']] #easier using loc

#Choosing between loc and iloc

#When choosing or transitioning between loc and iloc, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.
#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

reviews.set_index("title")  #This is useful if you can come up with an index for the dataset which is better than the current one.

reviews.country == 'Italy'   #producing a Series

reviews.loc[reviews.country == 'Italy'] #selection

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

reviews.loc[reviews.country.isin(['Italy', 'France'])]

reviews.loc[reviews.price.notnull()]

reviews['critic'] = 'everyone'   #setting a constant value Series
reviews['critic']

reviews['index_backwards'] = range(len(reviews), 0, -1)   # setting with an iterable of values:
reviews['index_backwards']

