from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Ethical response engine
def generate_response(dilemma, perspective):

    # --- Emotional Detection ---
    emotional_prefix = ""
    lower_dilemma = dilemma.lower()

    if any(word in lower_dilemma for word in ["scared", "afraid", "fear"]):
        emotional_prefix = (
            "It sounds like this situation is causing you fear or anxiety. "
            "That emotional weight matters deeply.\n\n"
        )

    elif any(word in lower_dilemma for word in ["confused", "lost", "unsure"]):
        emotional_prefix = (
            "It seems you're feeling uncertain, which is completely natural "
            "in complex moral situations.\n\n"
        )

    elif any(word in lower_dilemma for word in ["angry", "frustrated"]):
        emotional_prefix = (
            "There appears to be frustration or anger in this dilemma. "
            "Strong emotions often signal deeply held values.\n\n"
        )

    # --- Perspective Logic ---

    if perspective == "utilitarian":
        return emotional_prefix + f"""
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
        return emotional_prefix + f"""
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
        return emotional_prefix + f"""
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
    data = request.get_json()
    dilemma = data.get("message")
    perspective = data.get("perspective")

    response = generate_response(dilemma, perspective)

    return jsonify({"reply": response})


# IMPORTANT: This makes it work on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
