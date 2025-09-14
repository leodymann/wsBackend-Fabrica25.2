# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /code

# Copy requirements first
COPY requirements.txt /code/

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /code/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000
EXPOSE 8000

# Run Django
CMD ["python", "openlibrary_crud/manage.py", "runserver", "0.0.0.0:8000"]

