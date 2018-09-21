# Dockerfile

FROM python:2.7

COPY . /app

WORKDIR /app

run pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
