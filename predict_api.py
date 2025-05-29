from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Allow frontend access (replace with actual Vercel frontend URL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["www.statstreak-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve BoxIQ player stats
@app.get("/api/boxiq")
async def get_boxiq():
    file_path = os.path.join(os.path.dirname(__file__), "boxiq_player_stats.json")
    with open(file_path) as f:
        data = json.load(f)
    return JSONResponse(content=data)

# Serve DvP stats
@app.get("/api/dvp")
async def get_dvp():
    file_path = os.path.join(os.path.dirname(__file__), "dvp_stats.json")
    with open(file_path) as f:
        data = json.load(f)
    return JSONResponse(content=data)
