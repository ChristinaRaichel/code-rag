FROM python:3.10.11

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .

EXPOSE 8000

