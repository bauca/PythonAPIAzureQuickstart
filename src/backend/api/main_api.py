from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the (Python+FastAPI, Docker, CI/CD, Azure: Pipelines, DevOps, Cloud) - Template v0.0.1"}

@app.get("/notcovered")
async def notcovered():
    return {"message": "Example of a non covered code"}