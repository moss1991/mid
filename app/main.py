# -*- coding: utf-8 -*- 
import os,sys
absolute_path = os.path.abspath(__file__)
catlog = os.path.dirname(absolute_path)
base_dir = os.path.dirname(catlog)
sys.path.insert(0,base_dir)

# fastapi
import uvicorn
from fastapi import FastAPI
from app.routers import webinfo,stockinfo,futuresinfo
from fastapi.middleware.cors import CORSMiddleware 

def create_app():
    app	= FastAPI()
    return app

app = create_app()

@app.on_event('startup')
def init_scheduler():
    pass

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    # allow_origins=origins,
)

app.include_router(
    webinfo.router,
    prefix="/webinfo",
    tags=["webinfo"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    stockinfo.router,
    prefix="/stockinfo",
    tags=["stockinfo"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    futuresinfo.router,
    prefix="/futuresinfo",
    tags=["futuresinfo"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

if __name__ == "__main__":
    uvicorn.run(
        app='main:app', host="127.0.0.1", port=8081, 
        # workers=5, 
        # reload=True, debug=True
    )