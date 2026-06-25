from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
import os
from gui.mcp_client import call_tool

app = FastAPI()

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")


templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

class ToolRequest(BaseModel):
    tool_name: str
    arguments: dict

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name = "index.html")

@app.post("/run-tool")
async def run_tool(request: ToolRequest):
    result = await call_tool(request.tool_name, request.arguments)
    return {"result": result.content[0].text}
