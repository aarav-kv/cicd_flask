
# this is the base image
FROM python:3.10

# creates a flaskapi-app folder in the container.
WORKDIR /flaskapi-app

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
