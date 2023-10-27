import pandas as pd
from fastapi import APIRouter

router = APIRouter()

# Should return the user who accumulates the most played hours for the given genre and a list of the accumulation of played hours per year.
@router.get("/most_played_user_by_genre_slow/{genre}")
def most_played_user_by_genre_slow(genre: str):
    # Read the dataframes
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    df_user_items = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_items.parquet', engine='pyarrow')

    # Filter the games dataframe by the genre
    df_games_genre = df_games[df_games['genres'].apply(lambda x: genre in x)]

    # Join the user items with the games data
    df_user_genre = pd.merge(df_user_items, df_games_genre, left_on='item_id', right_on='id', how='inner')

    # Calculate the total playtime for all games of the given genre
    total_playtime = df_user_genre['playtime_forever'].sum()

    # Group by user_id and calculate the total playtime
    df_user_playtime = df_user_genre.groupby('user_id')['playtime_forever'].sum()

    # Find the user with the maximum playtime
    max_playtime_user = df_user_playtime.idxmax()

    # Group by release year and calculate the total playtime
    df_user_genre['release_year'] = pd.to_datetime(df_user_genre['release_date']).dt.year
    playtime_per_year = df_user_genre.groupby('release_year')['playtime_forever'].sum()

    return max_playtime_user, playtime_per_year, total_playtime

# Should return the user who accumulates the most played hours for the given genre and a list of the accumulation of played hours per year.
@router.get("/most_played_user_by_genre/{genre}")
def most_played_user_by_genre(genre: str):
    # Read the dataframes
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
    df_user_items = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_items.parquet', engine='pyarrow')

    # Filter the games dataframe by the genre
    df_games_genre = df_games[df_games['genres'].apply(lambda x: genre in x)]

    # Filter the user items dataframe to include only the items that correspond to the games of the given genre
    df_user_items_genre = df_user_items[df_user_items['item_id'].isin(df_games_genre['id'])]

    # Calculate the total playtime for all games of the given genre
    total_playtime = df_user_items_genre['playtime_forever'].sum()

    # Join the user items with the games data
    df_user_genre = pd.merge(df_user_items_genre, df_games_genre, left_on='item_id', right_on='id', how='inner')

    # Group by user_id and calculate the total playtime
    df_user_playtime = df_user_genre.groupby('user_id')['playtime_forever'].sum()

    # Find the user with the maximum playtime
    max_playtime_user = df_user_playtime.idxmax()

    # Group by release year and calculate the total playtime
    df_user_genre['release_year'] = pd.to_datetime(df_user_genre['release_date']).dt.year
    playtime_per_year = df_user_genre.groupby('release_year')['playtime_forever'].sum()

    # Return a dictionary
    return {
        "max_playtime_user": max_playtime_user,
        "playtime_per_year": playtime_per_year.to_dict(),
        "total_playtime": total_playtime
    }

# test

print(most_played_user_by_genre('Action'))
# max_playtime_user, playtime_per_year, total_playtime = most_played_user_by_genre('Action')
# print(f"User with maximum playtime: {max_playtime_user}")
# print(f"Playtime per year: {playtime_per_year}")
# print(f"Total playtime: {total_playtime}")
