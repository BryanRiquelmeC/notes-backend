from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


#confiurando CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: cambiar a la url de frontend, para mejorar la seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

#Endpoit basico "Hello, World"

@app.get("/")
def hello_world():
    return {"message": "Hello World- AGAIN!"}