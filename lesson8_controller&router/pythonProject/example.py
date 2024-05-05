from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()


def check_input(name: str):
    return name == "sara"


@app.get("/example")
async def get_user(is_authenticated: bool = Depends(check_input)):
    if is_authenticated:
        return "great"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")
