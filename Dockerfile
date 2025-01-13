# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy application code to the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install flask pillow werkzeug pandas

# Create required directories
#RUN mkdir -p templates certificates uploads fonts

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "main.py", "-c", "config"]
