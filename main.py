from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from api.routes import router

app = FastAPI()

app.include_router(router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )