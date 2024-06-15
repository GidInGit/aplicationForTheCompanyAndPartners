FROM python:slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Creates new user
RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown -R appuser /app

# Install deps
RUN apt update && apt full-upgrade -y

# Install pip requirements
RUN pip install -U pip setuptools wheel
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

USER appuser

CMD ["fastapi", "run", "src/main.py"]
