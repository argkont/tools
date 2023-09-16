from typing import Union
from fastapi import FastAPI
from deep_translator import GoogleTranslator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message":"Hello {name}"}

@app.get("/tools/translate")
async def get_lang(keys: Union[str,None] = None,lng:Union[str,None] = None):
    translated = GoogleTranslator(source='auto', target=lng).translate(keys)
    return {translated}