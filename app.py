from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/plan", methods=["POST"])
def plan():
    data = request.get_json(force=True)
    goal = data.get("goal", "").strip()

    if not goal:
        return jsonify({"error": "Goal is required"}), 400

    # Very naive placeholder planner
    steps = [
        f"Analyze intent: {goal}",
        f"Search memory for context",
        f"Apply tone filter to final result",
        f"Run core-text for final generation"
    ]

    return jsonify({"plan": steps})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "🧭 Planner node online."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
