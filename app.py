import pickle
from flask import Flask, render_template, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()
secret = os.getenv("SECRET_KEY")

app = Flask(__name__)

# 🔹 Load chatbot data (X, answers, vectorizer, questions)
with open("chatbot_model.pkl", "rb") as f:
    X, answers, vectorizer, questions = pickle.load(f)

def get_response(user_input):
    # Convert input to vector
    user_vec = vectorizer.transform([user_input])

    # Compute similarity
    sim = cosine_similarity(user_vec, X)
    idx = sim.argmax()

    # Confidence threshold
    if sim[0][idx] < 0.3:
        return "Sorry, I don’t understand that yet."

    return answers[idx]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/videoresume")
def videoresume():
    return render_template("videoresume.html")

@app.route("/projectML")
def project_ml():
    return render_template("projectML.html")

@app.route("/webDev")
def web_dev():
    return render_template("webDev.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    user_message = data.get("message", "")

    bot_reply = get_response(user_message)

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

