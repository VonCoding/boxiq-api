from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
import os

app = FastAPI()

# ✅ Replace this with your actual deployed frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://statstreak.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Endpoint to serve boxiq_player_stats.json
@app.get("/api/boxiq")
async def get_boxiq():
    with open("data/boxiq_player_stats.json") as f:
        data = json.load(f)
    return JSONResponse(content=data)

# ✅ Endpoint to serve dvp_stats.json
@app.get("/api/dvp")
async def get_dvp():
    with open("data/dvp_stats.json") as f:
        data = json.load(f)
    return JSONResponse(content=data)

# ✅ Predict endpoint for BoxIQ
class PredictionInput(BaseModel):
    player_name: str
    stat_type: str
    line: float
    odds: int
    choice: str

@app.post("/api/predict")
async def get_prediction(data: PredictionInput):
    # Placeholder BoxIQ logic
    return {
        "confidence": 71,  # Simulated confidence
        "message": f"Prediction calculated for {data.player_name} - {data.stat_type}"
    }

@app.get("/")
async def root():
    return {"message": "BoxIQ FastAPI is running"}
