# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Flask and psycopg2-binary
RUN pip install Flask psycopg2-binary

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables (can be overridden during runtime)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run app.py when the container launches
CMD ["python", "app.py"]
