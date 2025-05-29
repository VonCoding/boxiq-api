# BoxIQ Prediction API (Render Ready)

## 🔧 How to Deploy on Render
1. Go to [Render.com](https://render.com)
2. Create a new Web Service
3. Connect this repo or upload manually
4. Use `uvicorn predict_api:app --host 0.0.0.0 --port 10000` as start command
5. Set Python version to 3.9+

## 📁 Files
- `boxiq_model.py`: Core confidence logic
- `predict_api.py`: FastAPI app
- `data/boxiq_player_stats.json` → Upload this manually
- `data/dvp_stats.json` → Upload this manually