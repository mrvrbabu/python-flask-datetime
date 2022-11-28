# Use below python base docker image
FROM python:3.10-slim-bullseye
ENV TZ="Asia/Kolkata"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /datetime

# Install pip requirements

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt 

COPY datetime /datetime

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]