from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from deep_translator import GoogleTranslator

app = FastAPI()


@app.get("/")
async def root():
    html_content="""
    <html>
    <body>
        <small>Tools for Mauro Rios.</small>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/tools/translate")
async def get_lang(keys: Union[str,None] = None,lng:Union[str,None] = None):
    translated = GoogleTranslator(source='auto', target=lng).translate(keys)
    return {translated}