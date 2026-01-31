FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN 

COPY . .

CMD ["python", "manage.py", "runserver", "0:8000", "--settings=newvc.settings.development"]