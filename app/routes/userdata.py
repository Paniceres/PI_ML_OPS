import pandas as pd
from fastapi import APIRouter
from memory_profiler import memory_usage 
import os 

router = APIRouter()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# It should return the amount of money spent by the user, the recommendation percentage based on reviews.recommend, and the number of items.
@router.get("/userdata/{user_id}")
def userdata(User_id : str):
    # Read only the necessary columns from the dataframes
    df_games = pd.read_parquet(os.path.join(script_dir, '../../data/steam_games.parquet'), columns=['price', 'id', 'app_name'], engine='pyarrow')
    df_user_reviews = pd.read_parquet(os.path.join(script_dir, '../../data/user_reviews.parquet'), columns=['user_id', 'item_id', 'recommend'], engine='pyarrow')
    df_user_items = pd.read_parquet(os.path.join(script_dir, '../../data/user_items.parquet'), columns=['user_id', 'item_id', 'item_name'], engine='pyarrow')

    # Filter the dataframes by user_id
    # df_user_reviews = df_user_reviews[df_user_reviews['user_id'] == User_id]
    # df_user_items = df_user_items[df_user_items['user_id'] == User_id]

    # Merge df_user_reviews and df_user_items on 'item_id' and 'user_id'
    df_user = pd.merge(df_user_reviews, df_user_items, on=['item_id'], how='inner')

    # Filter df_games to include only the games the user has bought
    df_games = df_games[df_games['id'].isin(df_user['item_id'])]

    # Merge df_user and df_games on 'item_id' and 'id'
    df_user_games = pd.merge(df_user, df_games, left_on='item_id', right_on='id', how='inner')

    # Delete the original dataframes to free up memory
    del df_games, df_user_reviews, df_user_items, df_user

    # Calculate the total number of items
    total_items = df_user_games['item_id'].nunique()

    # Calculate the total amount of money spent by the user
    total_money_spent = df_user_games['price'].sum()

    # Calculate the total reviews and total recommendations
    recommend_counts = df_user_games['recommend'].value_counts()
    if recommend_counts.empty:
        total_reviews = 0
        total_recommendations = 0
    else:
        if len(recommend_counts) == 2:
            total_reviews, total_recommendations = recommend_counts
        else:
            total_reviews = recommend_counts[0]
            total_recommendations = 0 if df_user_games['recommend'].iloc[0] else total_reviews

    # Calculate the percentage of recommendations
    recommendation_percentage = (total_recommendations / total_reviews) * 100 if total_reviews else 0

    # Return a dictionary
    return {
        "total_money_spent": int(total_money_spent),
        "recommendation_percentage": recommendation_percentage,
        "total_items": int(total_items)
    }

# # # Start measuring memory usage
# mem_usage_before = memory_usage(-1, interval=0.1, timeout=1)[0]

# # # Call func
# # # print(userdata('LydiaMorley'))
# print(userdata('evcentric'))
# # # print(userdata('Riot-Punch'))
# # print(userdata('Sp3ctre'))


# # # # End measuring memory usage
# mem_usage_after = memory_usage(-1, interval=0.1, timeout=1)[0]

# print(f"Memory used: {mem_usage_after - mem_usage_before} MB")

