FROM python:3.9

RUN curl -fsSL https://get.docker.com | sh
COPY . /tests

COPY requirements.txt /tests/requirements.txt
WORKDIR /tests

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

CMD ["python", "access_test.py"]


