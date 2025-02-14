from flask import Flask, jsonify
from flask_cors import CORS
from routes.recommendation import recommendation_bp

app = Flask(__name__)
CORS(app)  # Enable CORS

# Register API Blueprint
app.register_blueprint(recommendation_bp)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the 60-Day Personalized Diet Recommendation API!",
        "usage": "Send a POST request to /api/recommend with user details."
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
