# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy only the contents of src/api while keeping the structure
COPY ./app /app

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]
