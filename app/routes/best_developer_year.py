import pandas as pd
from fastapi import APIRouter

router = APIRouter()

@app.get("/top_developers/{year}")
def top_3_developers(year: str):
    df_user_reviews = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/user_reviews.parquet', engine='pyarrow')
    df_games = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')

    # Unir los dataframes
    df = df_user_reviews.merge(df_games, left_on='item_id', right_on='id', how='inner')

    # Filtrar por año y recomendaciones
    df = df[(df['release_date'] == year) & (df['recommend'] == True)]

    # Agrupar por desarrollador y contar las recomendaciones
    top_developers = df.groupby('developer').size().sort_values(ascending=False)

    # Tomar los primeros tres
    top_developers = top_developers[:3].reset_index()

    # Crear lista de diccionarios
    top_3 = []
    for i in range(3):
        top_3.append({f'Puesto {i+1}': top_developers.loc[i, 'developer']})

    return top_3

import requests
