import sys
sys.path.insert(0, '/home/p/Code/Henry/PI_ML_OPS/app/routes')
from fastapi import FastAPI, app
from .routes import router as user_for_genre_router, developer_router, userdata_router, top_developers_router

app = FastAPI()

app.include_router(user_for_genre_router)
app.include_router(developer_router)
app.include_router(top_developers_router)
app.include_router(userdata_router)



@app.get("/")
def read_root():
    return {"Hello": "World"}

# make pydantic models
# make some exceptions handlers

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    