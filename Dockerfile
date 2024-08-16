# Use the official Python image as a base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY . /app

# Expose the port Streamlit runs on
EXPOSE 8080

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
