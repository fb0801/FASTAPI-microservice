from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel 

app = FastAPI()

redis = get_redis_connection(
    host = '',
    port = 1184,
    password = '',
    decode_responses = True
    )

class Product():


@app.get("/")
def read_root():
    return {"Hello": "World"}