from display import main_function
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="html_files")

headers = ("Artist", "Album", "Release Date")

@app.get("/home", response_class=HTMLResponse)
def show_album_data(request: Request):
   data = main_function()
   return templates.TemplateResponse("index.html", {"request": request, "headers": headers, "data": data})

app.mount("/static", StaticFiles(directory="static"), name="static")
   

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)