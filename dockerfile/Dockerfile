FROM python:3.10.0-slim-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip 
COPY dockerfile/requirements.txt .
RUN pip install -r requirements.txt
COPY cache .
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
#RUN python3 manage.py rqworker default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]