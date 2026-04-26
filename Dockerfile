# Use an official Python runtime as a parent image
FROM python:3.13-slim-trixie

# Set the working directory to /app
WORKDIR /app

# Install dependencies first (cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . /app

# Run app.py when the container launches
ENTRYPOINT ["python", "fx_rate.py"]
