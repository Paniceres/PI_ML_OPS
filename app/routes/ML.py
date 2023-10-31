import pandas as pd
import numpy as np
from surprise import SVD
from surprise import accuracy
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
import pickle
from fastapi import APIRouter
import os




router = APIRouter()

@router.get("/recommend/{user_id}")
def recommend(user_id: str):
    # Get the absolute path to the 'data' directory
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
    
    # Load df_user_reviews, games, and model from their respective files in PI_ML_OPS/data
    df_user_reviews = pd.read_parquet(os.path.join(data_dir, 'ML_df.parquet'))

    # Load games from its file in PI_ML_OPS/data
    games = pd.read_parquet(os.path.join(data_dir, 'ML_unique_games.parquet'))['game'].tolist()

    # Load the trained model from pickle file
    with open(os.path.join(data_dir, "ML_model.pkl"), 'rb') as model_file:
        model = pickle.load(model_file) 
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


# print(recommend('doctr'))