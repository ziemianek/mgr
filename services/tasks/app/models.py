from pydantic import field_validator
from sqlmodel import Field, SQLModel
from typing import Optional


class BaseTask(SQLModel):
    """
    Pydantic model for the task schema.
    """
    task_name: str
    task_description: Optional[str] = ""
    task_completed: bool = False


class Task(BaseTask, table=True):
    """
    Pydantic model for the task schema.
    """
    task_id: Optional[str] = Field(default=None, primary_key=True)


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
