import sys
sys.path.insert(0, './app/routes')
from fastapi import FastAPI
from routes import router as routes_router

app = FastAPI()

app.include_router(routes_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)