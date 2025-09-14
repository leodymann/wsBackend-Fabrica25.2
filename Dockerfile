# python base image
FROM python:3.12-slim

# Working directory container
WORKDIR /code

# copy requirements file
COPY requirements.txt /code/

# install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip and install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /code/

# avoid environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# expose port 8000
EXPOSE 8000

# run the application
CMD ["python", "book_manager/openlibrary_crud/manage.py", "runserver", "0.0.0.0:8000"]
