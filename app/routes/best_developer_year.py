import pandas as pd
from fastapi import APIRouter
import os

router = APIRouter()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

@router.get("/top_developers/{year}")
def top_3_developers(year: str):

    # Read only the necessary columns from the dataframes
    df_games = pd.read_parquet(os.path.join(script_dir, '../../data/steam_games.parquet'), columns=['release_date', 'id', 'app_name', 'developer'], engine='pyarrow')
    df_user_reviews = pd.read_parquet(os.path.join(script_dir, '../../data/user_reviews.parquet'), columns=['user_id', 'item_id', 'recommend'], engine='pyarrow')

    # Merge the dataframes
    df = df_user_reviews.merge(df_games, left_on='item_id', right_on='id', how='inner')

    # Filter by year and recommendations
    df = df[(df['release_date'] == year) & (df['recommend'] == True)]

    # Group by developer and count the recommendations
    top_developers = df.groupby('developer').size().sort_values(ascending=False)

    # If less than 3 developers published games, return an error message
    if len(top_developers) < 3:
        return {"error": f"Less than 3 developers published games in the year {year}."}

    # If there are no reviews for the given year, return an error message
    if df.empty:
        return {"error": f"No reviews found for the year {year}."}
    
    # Take the top three
    top_developers = top_developers[:3].reset_index()

    # Create a list of dictionaries
    top_3 = []
    for i in range(3):
        top_3.append({f'Position {i+1}': top_developers.loc[i, 'developer']})

    return top_3

print(top_3_developers('2018'))