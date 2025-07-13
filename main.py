
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

class User(BaseModel):
    username: str
    password: str

@app.post("/signup")
def signup(user: User):
    return {"message": "Signup successful", "user": user.username}

@app.post("/login")
def login(user: User):
    if user.username == "admin" and user.password == "admin":
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Invalid credentials")
# Temporary in-memory user storage
users = {}

@app.post("/signup")
def signup(user: User):
    users[user.username] = user.password
    return {"message": "Signup successful", "user": user.username}

@app.post("/login")
def login(user: User):
    if user.username in users and users[user.username] == user.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Invalid credentials")
