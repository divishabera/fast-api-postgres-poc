from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

from main import * 


app = FastAPI()

class NoteIn(BaseModel): #this model is used to send TO postgres
    text: str
    completed: bool

class Note(BaseModel): #this model is used to receive FROM postgres
    id: int
    text: str
    completed: bool


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {"message": "Welcome to the divi's app."}


@app.get("/notes/", tags=["Notes"], response_model=List[Note], status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    #await database.connect()
    query = notes.select().offset(skip).limit(take)
    return await database.fetch_all(query)


@app.post("/notes/", tags=["Notes"],response_model=Note, status_code = status.HTTP_201_CREATED)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}    