import os
from dotenv import dotenv_values


def get_env_vars_from_file(env_vars_file: str = ".env") -> dict[str, str]:
    """
    Reads environment variables from a specified file and returns them as a dictionary.

    Args:
        env_vars_file (str): The path to the environment variables file. Defaults to ".env".

    Returns:
        dict[str, str]: A dictionary containing the environment variables as key-value pairs.

    Raises:
        FileNotFoundError: If the specified environment variables file does not exist.
    """
    if not os.path.isfile(env_vars_file):
        raise FileNotFoundError(f"File {env_vars_file} not found")

    return dotenv_values(env_vars_file)
