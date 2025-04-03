from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from controller.operators import operator_router as operators
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="view")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(operators, prefix="/operators")

@app.get("/")
async def root():
    return templates.TemplateResponse("index.html" , {"request": {}})
    
