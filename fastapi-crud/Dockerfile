FROM python:3.8

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt


# set env variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

EXPOSE 9090
#CMD ["python", "main.py"]

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]

#warning: not maintaining this anymore
#note: at this point dockerfile is not of use, this was used before postgres was integrated for crud. Use docker compose now.