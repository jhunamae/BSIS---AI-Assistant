from flask import Flask, request, render_template
import json
from fuzzywuzzy import process

# Load knowledge base
with open("data.json", "r") as file:
    knowledge_base = json.load(file)

app = Flask(__name__)

def answer_question(question):
    question = question.lower().strip()
    best_match, score = process.extractOne(question, knowledge_base.keys())

    if score >= 80:
        result = knowledge_base[best_match]
        responses = []

        # If it's just a string (old format), make it into one entry
        if isinstance(result, str):
            responses.append({"text": result})
        else:
            i = 1
            while True:
                text_key = f"answer{i}" if i > 1 else "answer"
                img_key = f"image{i}" if i > 1 else "image"

                if text_key not in result and img_key not in result:
                    break

                entry = {}
                if text_key in result:
                    entry["text"] = result[text_key]
                if img_key in result:
                    entry["image"] = result[img_key]

                responses.append(entry)
                i += 1

        return responses, []
    else:
        suggestions = [match for match, s in process.extract(question, knowledge_base.keys(), limit=3) if s >= 50]
        return [{"text": "It's Beyond the scope. This AI assistant focuses only on how we can help you with our Institution."}], suggestions



@app.route("/", methods=["GET", "POST"])
def index():
    response = []
    suggestions = []
    if request.method == "POST":
        user_question = request.form["question"]
        response, suggestions = answer_question(user_question)
    return render_template("index.html", response=response, suggestions=suggestions)


if __name__ == "__main__":
    app.run(debug=True)
