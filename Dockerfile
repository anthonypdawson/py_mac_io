
FROM python:3.11.1-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app
RUN apt-get update \
    && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python - --version 1.3.2
ENV PATH="$POETRY_HOME/bin:/root/.local/bin:$PATH"


COPY pyproject.toml poetry.lock *.md .env ./
COPY pymacio ./pymacio/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
ENTRYPOINT ["poetry", "--quiet", "run", "pymacio"]
