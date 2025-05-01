from flask import Flask, request, render_template
import json
from fuzzywuzzy import process

# Load knowledge base
with open("data.json", "r") as file:
    knowledge_base = json.load(file)

app = Flask(__name__)

def answer_question(question):
    question = question.lower().strip()
    result = process.extractOne(question, knowledge_base.keys())
    
    if result is None:
        return "Sorry, I couldn't understand your question and there are no suggestions available.", []

    best_match, score = result

    if score >= 90:
        return knowledge_base[best_match], []
    else:
        suggestions = [
            match for match, s in process.extract(question, knowledge_base.keys(), limit=3) if s >= 60
        ]
        # print("Suggestions:", suggestions)

        return (
            "It's beyond the scope. This AI assistant focuses only on questions related to the BSIS Department, If you want me to create another model for other programs send message here. "
            "Please clarify your question or see the suggestions below. If there's no suggestions that means no data/datas related of what you prompt",
            suggestions
        )

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    suggestions = []
    if request.method == "POST":
        user_question = request.form["question"]
        response, suggestions = answer_question(user_question)
    return render_template("index.html", response=response, suggestions=suggestions)


if __name__ == "__main__":
    app.run(debug=True)
