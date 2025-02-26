from fastapi import APIRouter
from .user_for_genre import most_played_user_by_genre
from .userdata import userdata
from .best_developer_year import top_3_developers
from .developer import developer
from .developer_recommendations import developer_rec
from .ML import recommend
router = APIRouter()

@router.get("/most_played_user_by_genre/{genre}")
def get_most_played_user_by_genre(genre: str):
    return most_played_user_by_genre(genre)

@router.get("/developer/{developer}")
def get_developer_data(dev_name: str):
    return developer(dev_name)

@router.get("/top_developers/{year}")
def get_top_3_developers(year: str):
    return top_3_developers(year)

@router.get("/userdata/{user_id}")
def get_user_data(user_id: str):
    return userdata(user_id)

@router.get("/developer_rec/{developer}")
def get_developer_rec(dev_name: str):
    return developer_rec(dev_name)

@router.get("/recommend/{user_id}")
async def get_recommend(user_id: str):
    return recommend(user_id)