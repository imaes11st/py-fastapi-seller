from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Configuracion Fast API"}
