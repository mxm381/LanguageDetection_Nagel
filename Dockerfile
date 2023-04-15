FROM python:3.8-slim-buster

WORKDIR /app

COPY webapp /app/webapp
COPY /webapp/pyproject.toml /app/
COPY /webapp/poetry.lock /app/
COPY /README.md /app/

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN pip install pyodbc

RUN pip install azure-ai-textanalytics
RUN pip install azure-core

RUN pip install flask
RUN pip install poetry
RUN poetry install --no-dev

EXPOSE 5000

CMD [ "python", "./webapp/app.py" ]