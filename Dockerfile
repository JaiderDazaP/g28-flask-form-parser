# Dockerfile
FROM python:3.12-slim


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set PYTHONPATH for pytest to find the app package
ENV PYTHONPATH=/app

# Run tests when the container is built
RUN pytest --disable-warnings

# Run the Flask server
CMD ["python", "app/main.py"]
