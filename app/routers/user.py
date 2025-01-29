from fastapi import APIRouter

# Создаем роутер для пользователей
router = APIRouter(prefix="/user", tags=["user"])


# Маршрут для получения всех пользователей
@router.get("/")
async def all_users():
    pass


# Маршрут для получения пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass


# Маршрут для создания нового пользователя
@router.post("/create")
async def create_user():
    pass


# Маршрут для обновления данных пользователя
@router.put("/update")
async def update_user():
    pass


# Маршрут для удаления пользователя
@router.delete("/delete")
async def delete_user():
    pass