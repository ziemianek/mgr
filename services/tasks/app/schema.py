from pydantic import BaseModel

class BaseTask(BaseModel):
    task_id: int
    task_name: str
    task_description: str
    completed: bool

# class CreateTask(BaseTask):
#     pass

# class UpdateTask(BaseTask):
#     pass

# class DeleteTask(BaseTask):
#     pass
