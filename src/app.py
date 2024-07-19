from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


app = FastAPI(
    title='Test API',
    description='A simple test API',
    version='0.0.1'
)

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "http://localhost:8000/users/1"
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



client = MongoClient("mongodb://localhost:27017")
db = client['Einaki']
users = db['Users']

print("users:: ", users.find_one({'userId': '1'})) 
print(db.list_collection_names())

@app.get('/users/{userId}')
async def getUser(userId: str):
    return users.find_one({'userId': userId})


# https://www.youtube.com/watch?v=PW1RhQPuQxc&t=1953s