# Use official Python image
FROM python:3.10-slim

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Move into src directory where manage.py exists
WORKDIR /app/src

# Collect static files
RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

# Run server
CMD ["gunicorn", "wms.wsgi:application", "--bind", "0.0.0.0:8000"]
