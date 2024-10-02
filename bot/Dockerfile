FROM python:3.12.7-alpine3.20
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN python -m pip install discord.py python-dotenv
ENV PYTHONBUFFERED 1
COPY . .
CMD python3 -m main.py