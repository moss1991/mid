# -*- coding: utf-8 -*- 
import os,sys
absolute_path = os.path.abspath(__file__)
catlog = os.path.dirname(absolute_path)
base_dir = os.path.dirname(catlog)
sys.path.insert(0,base_dir)

# fastapi
import uvicorn
from fastapi import FastAPI
from app.routers import web,stock,futures,haiguan,econ
from fastapi.middleware.cors import CORSMiddleware 

# models.Base.metadata.create_all(bind=engine)

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
    web.router,
    prefix="/api/web",
    tags=["web"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    stock.router,
    prefix="/api/stock",
    tags=["stock"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    futures.router,
    prefix="/api/futures",
    tags=["futures"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    haiguan.router,
    prefix="/api/haiguan",
    tags=["haiguan"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    econ.router,
    prefix="/api/econ",
    tags=["econ"],
    # dependencies=[Depends(corpauth.get_token_header)],
    responses={404: {"description": "Not found"}},
)


if __name__ == "__main__":
    uvicorn.run(
        app='main:app', host="127.0.0.1", port=8081, 
        # workers=5, 
        # reload=True, debug=True
    )