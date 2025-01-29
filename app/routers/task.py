from fastapi import APIRouter

# Создаем роутер для задач
router = APIRouter(prefix="/task", tags=["task"])

# Маршрут для получения всех задач
@router.get("/")
async def all_tasks():
    pass

# Маршрут для получения задачи по ID
@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass


# Маршрут для создания новой задачи
@router.post("/create")
async def create_task():
    pass


# Маршрут для обновления задачи
@router.put("/update")
async def update_task():
    pass


# Маршрут для удаления задачи
@router.delete("/delete")
async def delete_task():
    pass