FROM python:3.9

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
