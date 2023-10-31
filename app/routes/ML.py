import pandas as pd
import numpy as np
from surprise import SVD
from surprise import accuracy
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
import pickle
from fastapi import APIRouter

router = APIRouter()

# Load the user reviews and steam games data from a parquet file using the pyarrow engine
df_user_reviews = pd.read_parquet('../../data/user_reviews.parquet', engine='pyarrow')
df_games = pd.read_parquet('../../data/steam_games.parquet', engine='pyarrow')

# Select only the desired columns
df_reviews = df_user_reviews[['user_id', 'item_id', 'sentiment_score', 'recommend']]
df_games = df_games[['id', 'app_name']]

# Merge df_games and df_user_reviews
df = df_reviews.merge(df_games, left_on='item_id', right_on='id', how='inner')

# Selecting the columns to be used for the algorithm, dropping the following columns
df.drop(['id', 'item_id', 'sentiment_score', 'recommend'], inplace=True, axis=1)

# Create a new dataframe 'model' with only 'user_id', 'app_name', and 'rating'
model = df[['user_id', 'app_name', 'rating']]

# Load the trained model when the application starts
with open("ML_model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

# Get a list of unique game names from the 'app_name' column of the dataframe
games = df["app_name"].unique()

@router.get("/recommend/{user_id}")
async def recommend(user_id: str):
    # Get the list of games played by the user
    played_games = df_user_reviews[df_user_reviews['user_id'] == user_id]['app_name'].unique()

    # Create a list of games that have not been played by subtracting the set of played games from the set of all games
    not_played_games = list(set(games) - set(played_games))

    # Use the trained model to predict the ratings of the games not played by the user
    predic_not_played = [model.predict(user_id, line) for line in not_played_games]

    # Sort the predictions in descending order of estimated rating and select the top 5 as recommendations
    top5_recomm = sorted(predic_not_played, key=lambda x: x.est, reverse=True)[:5]

    # Create an empty dictionary 'games_dict'
    games_dict = {}

    # Loop through the top 5 recommendations. For each recommendation, add a new entry to the dictionary with the key as 'game {i}' and the value as the game's ID
    for i, rec in enumerate(top5_recomm, start=1):
        games_dict[f'game {i}'] = rec.iid

    return games_dict