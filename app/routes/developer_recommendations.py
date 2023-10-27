import pandas as pd
from fastapi import APIRouter

router = APIRouter()

@router.get("/developer_rec/{dev_name}")
def developer_rec(dev_name: str):
    # Read only the necessary columns from the dataframes
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', columns=['id', 'developer'], engine='pyarrow')
    df_user_reviews = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_reviews.parquet', columns=['item_id', 'sentiment_score'], engine='pyarrow')

    # Merge the two dataframes on item_id
    merged_df = pd.merge(df_user_reviews, df_games, left_on='item_id', right_on='id')

    # Filter the dataframe to only include rows for the specified developer
    dev_df = merged_df[merged_df['developer'] == dev_name]

    # Get the count of each sentiment score
    sentiment_counts = dev_df['sentiment_score'].value_counts().to_dict()

    # Return a dictionary with the developer name as the key and the sentiment counts as the value
    return {dev_name: sentiment_counts}

print(developer_rec("Valve"))
