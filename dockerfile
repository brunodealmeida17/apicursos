FROM python:3.9-slim


WORKDIR /app

RUN apt-get update && apt-get upgrade -y tzdata postgresql-client

ENV TZ=America/Sao_Paulo

COPY requeriments.txt requeriments.txt
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload"]

