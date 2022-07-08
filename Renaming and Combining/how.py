reviews.rename(columns={'points': 'score'})

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')