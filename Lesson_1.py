from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page():
    return {"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def users_page(user_id):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def users_info(username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


#python -m uvicorn Module_16.Lesson_1.Lesson_1:app