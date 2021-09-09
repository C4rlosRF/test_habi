FROM python:3.10.0b2-buster

RUN pip install mysql-connector && pip install fastapi uvicorn && pip install simplejson && pip install python-jose && pip install requests

EXPOSE 80

COPY ./ /app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
