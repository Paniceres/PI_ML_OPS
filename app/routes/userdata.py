import pandas as pd
from fastapi import APIRouter

router = APIRouter()

# It should return the amount of money spent by the user, the recommendation percentage based on reviews.recommend, and the number of items.
@router.get("/userdata_slow/{user_id}")
def userdata_slow(User_id : str):
    # Read the dataframes
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    df_user_reviews = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_reviews.parquet', engine='pyarrow')

    # Filter the user reviews dataframe by the user_id
    df_user = df_user_reviews[df_user_reviews['user_id'] == User_id]

    # Join the user reviews with the games data
    df_user_games = pd.merge(df_user, df_games, left_on='item_id', right_on='id', how='inner')

    # Calculate the total number of items
    total_items = df_user_games['item_id'].nunique()

    # Calculate the percentage of recommendations
    total_reviews = df_user_games.shape[0]
    total_recommendations = df_user_games[df_user_games['recommend'] == True].shape[0]
    recommendation_percentage = (total_recommendations / total_reviews) * 100

    # Calculate the total amount of money spent by the user
    total_money_spent = df_user_games['price'].sum()

    return total_money_spent, recommendation_percentage, total_items

# It should return the amount of money spent by the user, the recommendation percentage based on reviews.recommend, and the number of items.
@router.get("/userdata/{user_id}")
def userdata(User_id : str):
    # Read the dataframes
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    df_user_reviews = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_reviews.parquet', engine='pyarrow')

    # Filter the user reviews dataframe by the user_id
    df_user = df_user_reviews[df_user_reviews['user_id'] == User_id]

    # Filter the games dataframe to include only the games the user has reviewed
    df_games = df_games[df_games['id'].isin(df_user['item_id'])]

    # Join the user reviews with the games data
    df_user_games = pd.merge(df_user, df_games, left_on='item_id', right_on='id', how='inner')

    # Calculate the total number of items
    total_items = df_user_games['item_id'].nunique()

    # Calculate the total reviews and total recommendations
    recommend_counts = df_user_games['recommend'].value_counts()
    if len(recommend_counts) == 2:
        total_reviews, total_recommendations = recommend_counts
    else:
        total_reviews = recommend_counts[0]
        total_recommendations = 0 if df_user_games['recommend'].iloc[0] else total_reviews

    # Calculate the percentage of recommendations
    recommendation_percentage = (total_recommendations / total_reviews) * 100

    # Calculate the total amount of money spent by the user
    total_money_spent = df_user_games['price'].sum()

    return total_money_spent, recommendation_percentage, total_items



# test
# total_money_spent, recommendation_percentage, total_items = userdatav2('LydiaMorley')
# print(f"Total money spent: {total_money_spent}")
# print(f"Recommendation percentage: {recommendation_percentage}")
# print(f"Total items: {total_items}")