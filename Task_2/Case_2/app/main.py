# uvicorn main:app

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import random
import json


app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "app/static"),
    name="static",
)
templates = Jinja2Templates(directory="templates")

#редирект по сгенерированному адресу
@app.get('/{link}')
async def redirect(link: str):
    url_arr = await open_Json()

    for j in url_arr:
        if url_arr[j].split('/')[-1] == link:
            return RedirectResponse(j)

    return RedirectResponse('/')

# View
@app.get('/')
async def main_view(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})




@app.post("/")
async def get_url(request: Request, url: str = Form("")):
    return templates.TemplateResponse("link_block.html", {"request": request, "url": await generate_url(url)})


async def open_Json():
    with open('urls.json') as j:
        url_arr = json.load(j)
        return url_arr


async def generate_url(url):

    # Проверка на сущестующий URL
    url_arr = await open_Json()
    for j in url_arr:
        if j == url:
            return url_arr[j]
    old_url = url

    # генерация уникального адреса
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    link = ''

    for i in range(6):
        link += random.choice(chars)
    new_url = f"http://localhost:8000/{link}"

    # запись в файл
    url_arr = await open_Json()
    url_arr[old_url] = new_url

    with open('urls.json', 'w') as j:
        json.dump(url_arr, j)

    return new_url
