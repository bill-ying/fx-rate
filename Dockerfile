# Use an official Python runtime as a parent image
FROM python:3.13-slim-trixie

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install requests package
RUN pip install -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "fx_rate.py"]
