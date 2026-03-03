from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Ethical response engine
def generate_response(dilemma, perspective):

    if perspective == "utilitarian":
        return f"""
From a utilitarian perspective, the central question is:
What action produces the greatest overall good?

In your situation — "{dilemma}" — the outcome must be evaluated
based on who benefits and who suffers.

If exposing the truth maximizes collective well-being,
even at personal cost, utilitarianism would support it.
However, if the damage outweighs the benefits,
a more cautious path may be justified.

The moral weight lies in consequences.
"""

    elif perspective == "deontological":
        return f"""
From a deontological perspective, morality is grounded in duty,
not outcomes.

In your situation — "{dilemma}" — the question becomes:
What is the right action regardless of consequences?

If honesty, justice, or fairness are moral duties,
then they must be upheld even if they lead to discomfort
or personal sacrifice.

Integrity is not negotiable in this framework.
"""

    elif perspective == "virtue":
        return f"""
From a virtue ethics perspective, this dilemma asks:
What kind of person do you want to become?

In facing — "{dilemma}" — the focus shifts
from rules and consequences to character.

Courage, honesty, compassion, and wisdom
are the guiding traits.

The right action is the one that reflects
your highest moral self.
"""

    else:
        return "Select a philosophical lens to begin."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    dilemma = request.json.get("message")
    perspective = request.json.get("perspective")

    response = generate_response(dilemma, perspective)

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
