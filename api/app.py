import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

import os

app = Flask(__name__, 
            template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
            static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets')))

SYSTEM_PROMPT = """You are NutriAI, a specialized AI nutrition agent focused on Indian dietary habits and cuisine.
You have deep knowledge of:
- Traditional Indian foods, spices, and cooking methods
- Regional Indian diets (North, South, East, West India)
- Ayurvedic nutrition principles
- Indian festivals and their traditional foods
- Balancing macronutrients using common Indian ingredients (dal, roti, rice, sabzi, curd, etc.)
- Managing health conditions (diabetes, hypertension, PCOD, thyroid) through Indian diet
- Calculating BMI and recommending diet plans accordingly
- Creating personalized meal plans for Indian families

Always respond in a friendly, helpful manner. Provide practical advice using ingredients easily available in Indian households.
When suggesting meals, include approximate calorie counts and key nutritional benefits.
Keep responses concise, structured, and actionable."""


def get_watsonx_client():
    credentials = Credentials(
        url=os.getenv("url"),
        api_key=os.getenv("IBM_CLOUD_API_KEY"),
    )
    return APIClient(credentials)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    try:
        client = get_watsonx_client()
        model = ModelInference(
            model_id=os.getenv("MODEL_ID", "meta-llama/llama-3-3-70b-instruct"),
            api_client=client,
            project_id=os.getenv("PROJECT_ID"),
            params={
                "max_new_tokens": 512,
                "temperature": 0.7,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
            },
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ]

        response = model.chat(messages=messages)
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
