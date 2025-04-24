from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def startseite():
    return {"message": "Willkommen bei GenomeLab!"}

