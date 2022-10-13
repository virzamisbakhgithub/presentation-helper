FROM python:3.6.15-slim

RUN apt update -y

RUN apt install busybox bash gcc -y

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
# RUN python3 -m venv mp_env && source mp_env/bin/activate
RUN pip install -r requirements.txt
RUN pip list

ENTRYPOINT ["python"]

CMD ["backCode.py"]