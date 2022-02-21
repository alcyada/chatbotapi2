FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip  -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD pip3 install "uvicorn[standard]"
CMD uvicorn main:app --host 0.0.0.0 --port 80
