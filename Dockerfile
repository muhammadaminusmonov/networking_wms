# Use official Python image
FROM python:3.10-slim

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run server
CMD ["gunicorn", "wms.wsgi:application", "--bind", "0.0.0.0:8000"]
