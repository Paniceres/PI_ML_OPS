import pandas as pd
from pandas_profiling import ProfileReport


 # Read the data files
df_games = pd.read_parquet('../data/steam_games.parquet', engine='pyarrow')
df_user_reviews = pd.read_parquet('../data/user_reviews.parquet', engine='pyarrow')
df_user_items = pd.read_parquet('../data/user_items.parquet', engine='pyarrow')

# Select only the desired columns
df_games = df_games[['id', 'genres', 'app_name']]
df_user_reviews = df_user_reviews[['user_id', 'item_id', 'sentiment_score']]
df_user_items = df_user_items[['user_id', 'item_id', 'playtime_forever']]

# Merge df_games and df_user_reviews
df = df_games.merge(df_user_reviews, left_on='id', right_on='item_id', how='inner')

# Merge the result with df_user_items
df = df.merge(df_user_items, on=['user_id', 'item_id'], how='inner')


# Make a Profile Report
ProfileReport(df, title='Profile Report')