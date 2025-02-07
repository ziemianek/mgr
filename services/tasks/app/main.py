from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Union, Annotated
from uuid import uuid4

from .schemas import  CreateTask, TaskWithID
from .example_data import TASKS


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint that returns the service name.

    Returns:
        dict[str, str]: A dictionary containing the service name.
    """
    return {
        "service_name:": "tasks",
    }


@app.get(f"/tasks")
async def get_tasks(
    id: Annotated[Optional[str], Query(min_length=36, max_length=36)] = None
) -> Union[TaskWithID, list[TaskWithID]]:
    """
    Retrieve tasks from the task list.

    Args:
        id (Optional[int]): The ID of the task to retrieve. If not provided, all tasks will be returned.

    Returns:
        Union[TaskWithID, list[TaskWithID]]: A single task with the specified ID if provided, otherwise a list of all tasks.

    Raises:
        fastapi.HTTPException: If a task with the specified ID is not found, a 404 HTTP exception is raised.
    """
    if id:
        task = next((TaskWithID(**task) for task in TASKS if task["task_id"] == id), None)
        if task is None:
            raise HTTPException(status_code=404)
        return task

    return [
        TaskWithID(**task) for task in TASKS
    ]


@app.post("/tasks")
async def create_task(task_data: CreateTask) -> TaskWithID:
    """
    This endpoint allows you to create a new task by providing the necessary task data.

    Args:
        task_data (CreateTask): The task data required to create a new task.

    Returns:
        TaskWithID: The created task with a unique ID.
    """
    id = str(uuid4())
    # model_dump() is a method that converts the Pydantic model to a dictionary
    # https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump
    new_task = TaskWithID(task_id=id, **task_data.model_dump()).model_dump()
    TASKS.append(new_task)
    return new_task
