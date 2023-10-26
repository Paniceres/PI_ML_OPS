import pandas as pd
from fastapi import APIRouter

router = APIRouter()

# Calculate the number of items and the percentage of free content per year according to the developer.
@router.get("/developer/{developer}")
def developer(developer : str):
    df = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    # Filter the dataframe by the developer
    df_developer = df[df['developer'] == developer]

    # Calculate the number of items per year
    items_per_year = df_developer.groupby('release_date').size()
    
    # Add a new column 'is_free' which is True if the price is 0.00 and False otherwise
    df_developer['is_free'] = df_developer['price'] == 0.00

    # Calculate the percentage of Free content per year
    free_content_per_year = df_developer.groupby('release_date')['is_free'].mean() * 100

    return items_per_year, free_content_per_year

# Calculate the number of items and the percentage of free content per year according to the developer.
@router.get("/developerv2/{developer}")
def developerv2(developer: str):
    df = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    # Filter the dataframe by the developer
    df_developer = df[df['developer'] == developer]

    # Calculate the number of items per year
    items_per_year = df_developer.groupby('release_date').size()

    # Calculate the percentage of Free content per year
    free_content_per_year = (df_developer[df_developer['price'] == 0.00].groupby('release_date').size() / items_per_year) * 100

    return items_per_year, free_content_per_year



# test
# items_per_year, free_content_per_year = developer('Dovetail Games')
# print("Items per year:\n", items_per_year)
# print("Free content per year (%):\n", free_content_per_year) 