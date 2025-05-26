#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="MindTrack Test API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MindTrack Test Server Running"}

@app.post("/api/auth/login")
async def test_login():
    return {"message": "Test login endpoint working"}

@app.get("/test")
async def test():
    return {"message": "Test endpoint working"}

if __name__ == "__main__":
    print("🚀 Starting MindTrack Test Server...")
    print("📧 Testing basic API functionality")
    uvicorn.run(app, host="0.0.0.0", port=8001)
