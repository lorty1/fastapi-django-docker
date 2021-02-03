FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get install default-libmysqlclient-dev 
RUN pip install -r requirements.txt
COPY . /app/