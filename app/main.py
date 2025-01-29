from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router

# Создаем приложение FastAPI
app = FastAPI()

# Главный маршрут
@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты
app.include_router(task_router)
app.include_router(user_router)