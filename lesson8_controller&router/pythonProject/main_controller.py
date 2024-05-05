from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from examples import example_router
from other import other_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# app.add_middleware(CORSMiddleware,allow_origins=['*'])
app.include_router(example_router, prefix='/examples')
app.include_router(other_router, prefix='/other')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event('startup')
async def print_something():
    print("something")


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
