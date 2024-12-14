# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Change directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY src/api .

# Expose the port the app runs on
EXPOSE 5050
# Define the command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5050", "--debug"]
