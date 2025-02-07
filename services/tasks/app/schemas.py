from pydantic import BaseModel, field_validator
from typing import Optional


class BaseTask(BaseModel):
    """
    Pydantic model for the task schema.
    """
    task_name: str
    task_description: Optional[str] = ""
    task_completed: bool = False


class TaskWithID(BaseTask):
    """
    Pydantic model for the task schema with an ID.
    """
    task_id: str


class CreateTask(BaseTask):
    """
    Attributes:
        task_name (str): The name of the task. Must be a non-empty string.
        task_description (Optional[str]): The description of the task

    Methods:
        task_name_validator(cls, value):
            Validates that the task_name is not an empty string.
            Raises:
                ValueError: If task_name is an empty string.
    """
    @field_validator("task_name")
    @classmethod
    def task_name_validator(cls, value):
        if not value:
            raise ValueError("task_name cannot be an empty string")
        return value


class UpdateTask(BaseTask):
    pass
