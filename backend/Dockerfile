FROM python:3.12

WORKDIR /app

COPY ./site/ /static

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN pip install gunicorn==20.1.0

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "newvc.wsgi"]