import json
import math

def calculate_implied_probability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def get_boxiq_confidence(player_stats, dvp_stat, line, odds, category, choice):
    avg = player_stats.get("averages", {}).get(category, 0)
    streak = player_stats.get("streaks", {}).get(category, "")
    hits = sum(1 for g in player_stats.get("recentGames", []) if g.get(category, 0) >= line)
    games = len(player_stats.get("recentGames", []))
    hit_rate = hits / games if games > 0 else 0

    implied_prob = calculate_implied_probability(odds)
    dvp_factor = max(0.75, min(1.25, (dvp_stat or avg) / avg)) if avg > 0 else 1

    adjusted_rate = hit_rate * dvp_factor
    confidence = adjusted_rate / implied_prob * 100 if implied_prob > 0 else 0
    confidence = max(1, min(confidence, 99))

    # Adjust based on line difficulty
    line_gap = (line - avg) if choice == "over" else (avg - line)
    confidence += line_gap * 2
    confidence = max(1, min(confidence, 99))

    recommendation = "Over" if confidence >= 60 else "Under" if confidence <= 40 else "Lean"
    explanation = f"Avg: {avg}, Hit Rate: {hit_rate:.2f}, DvP Adj: {dvp_factor:.2f}, Streak: {streak}"

    return {
        "confidence": round(confidence),
        "recommendation": recommendation,
        "explanation": explanation
    }