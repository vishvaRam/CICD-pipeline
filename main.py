from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "fastapi-cicd"}

@app.get("/home")
def home():
    return {"message": "Welcome to your CI/CD deployed app!"}
