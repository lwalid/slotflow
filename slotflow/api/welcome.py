from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return 'Bonjour tout le monde'