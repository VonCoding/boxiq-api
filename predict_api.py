from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from boxiq_model import get_boxiq_confidence

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("boxiq_player_stats.json") as f:
    player_stats = json.load(f)

with open("dvp_stats.json") as f:
    dvp_stats = json.load(f)

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    player_id = str(data["playerId"])
    stat = data["stat"]
    line = float(data["line"])
    odds = int(data["odds"])
    choice = data["choice"].lower()

    stats = player_stats.get(player_id)
    dvp_value = dvp_stats.get(stat, {}).get(stats.get("position", ""), 0)

    result = get_boxiq_confidence(stats, dvp_value, line, odds, stat, choice)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
