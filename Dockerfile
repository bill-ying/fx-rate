# Use an official Python runtime as a parent image
FROM python:3.12.1-slim-bookworm

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requests package
RUN pip install requests

# Run app.py when the container launches
ENTRYPOINT ["python", "fx_rate.py"]
