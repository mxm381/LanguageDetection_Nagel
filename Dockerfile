FROM python:3.8-slim-buster

WORKDIR /app

COPY webapp /app/webapp
COPY /webapp/pyproject.toml /app/
COPY /webapp/poetry.lock /app/
COPY /README.md /app/

RUN pip install azure-ai-textanalytics
RUN pip install azure-core

RUN pip install flask
RUN pip install poetry
RUN poetry install --no-dev

EXPOSE 5000

CMD [ "python", "./webapp/app.py" ]