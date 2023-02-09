import rook
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from app import router



app = FastAPI()
app.include_router(router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


rook.start(
    token='15fceae1c79b9fa8db7b7eb3f67fcfcd0184f7ec57c25b12701caf81c2df679a',
    labels={"env": "dev"}
)
