FROM tiangolo/uvicorn-gunicorn:python3.9


COPY . /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000","-k", "uvicorn.workers.UvicornWorker" , "main:app"]



