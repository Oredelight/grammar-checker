from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from api.routes import router
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

# Pre-initialize LanguageTool on startup
@app.on_event("startup")
async def startup_event():
    logger.info("Pre-initializing LanguageTool on startup...")
    try:
        from services.grammarchecker import _get_tool
        tool = _get_tool()
        if tool:
            logger.info("✓ LanguageTool pre-initialized successfully")
        else:
            logger.warning("LanguageTool initialization skipped (will fall back to AI)")
    except Exception as e:
        logger.error(f"Error pre-initializing LanguageTool: {e}")

app.include_router(router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )