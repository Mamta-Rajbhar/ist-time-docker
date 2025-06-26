# Use official Python image from Docker Hub
FROM python:3.9-slim

# Install pytz
RUN pip install pytz

# Copy the local code to the container
COPY app.py /app/app.py

# Set working directory
WORKDIR /app

# Run the Python script
CMD ["python", "app.py"]

