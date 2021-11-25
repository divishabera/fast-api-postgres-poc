import uvicorn
from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import os
import urllib
from pydantic import BaseModel

#uncomment below 2 lines and change host_server to localhost if you are trying to run from the cmd python main.py
#if __name__ == "__main__":
#   uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)#so you are saying inside app, run api.py. in simpler applications api might be in main.py itself, so in that case it will be main:app

#for the postgres connection
host_server = os.environ.get('host_server', 'db') #important: this name here 'db' should be the same as service db: at the dockercompose
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'testdatabase') #ensure that you have such a testbase btw
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'dbera')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'yourpword')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
#ie 'postgresql://db_username:db_password@host_server:db_server_port/database_name?sslmode=prefer'

#now create an instance of the database
database = databases.Database(DATABASE_URL)

#a sqlalchemy model
metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)



app = FastAPI(title="FastAPI - PostgreSQL Async EndPoints")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



