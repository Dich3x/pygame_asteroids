FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv
RUN pip install -r requirements.txt

COPY asteroid.py .
COPY asteroidfield.py .
COPY circleshape.py .
COPY player.py .
COPY shot.py .
COPY constants.py .
COPY main.py .

CMD ["python3", "main.py"]