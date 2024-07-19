from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Test API',
    description='A simple test API',
    version='0.0.1'
)

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags=['root'])
async def home() -> dict:
    return {'message': 'first fastapi app'}


@app.post('/create', description='A simple post request through this endpoint')
async def createUser(message: str):
    return JSONResponse(content={'message': message}, status_code=200)


# https://www.youtube.com/watch?v=PW1RhQPuQxc&t=1953s