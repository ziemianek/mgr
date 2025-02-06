from fastapi import FastAPI, HTTPException
from typing import Optional, Union

from .schema import BaseTask
from .example_data import TASKS


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "service_name:": "tasks",
    }


@app.get(f"/tasks")
async def get_tasks(id: Optional[int] = None) -> Union[BaseTask, list[BaseTask]]:
    if id:
        task = next((BaseTask(**task) for task in TASKS if task["task_id"] == id), None)
        if task is None:
            raise HTTPException(status_code=404)
        return task

    return [
        BaseTask(**task) for task in TASKS
    ]
