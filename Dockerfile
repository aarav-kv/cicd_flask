
FROM python:3.10

WORKDIR /flaskapi-app

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
 