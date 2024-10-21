from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
users = []
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post('/user/{username}/{age}')
async def users_info(username: str, age: int):
    new_user = User(id=len(users) + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    try:
        users[user_id - 1] = User(id=user_id, username=username, age=age)
        return users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was notfound")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    if user_id == users[user_id - 1].id:
        return users.pop(user_id - 1)
    else:
        raise HTTPException(status_code=404, detail="User was not found")
