import pandas as pd
from fastapi import APIRouter
import os

router = APIRouter()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Calculate the number of items and the percentage of free content per year according to the developer.
@router.get("/developer/{developer}")
def developer(developer : str):
    # Read the dataframe
    df_games = pd.read_parquet(os.path.join(script_dir, '../../data/steam_games.parquet'), columns=['release_date', 'id', 'developer', 'price'], engine='pyarrow')

    # Filter the dataframe by the developer
    df_developer = df_games[df_games['developer'] == developer]

    # Calculate the number of items per year
    items_per_year = df_developer.groupby('release_date').size()
    
    # Calculate the percentage of Free content per year
    free_content_per_year = (df_developer['price'] == 0.00).groupby(df_developer['release_date']).mean() * 100

    return {
        "items_per_year": items_per_year.to_dict(),
        "free_content_per_year": free_content_per_year.to_dict()
    }


# print(developer('Valve'))