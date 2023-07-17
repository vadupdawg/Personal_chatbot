from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import openai 
import os

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
@limiter.limit("10 per minute")
def chat():
    user_message = request.json.get('user_message')
    system_message = "Je bent de GroeimetAi-Personal chatbot. Je moet je voordoen als een werknemer van GroeimetAi, een bedrijf dat AI-gestuurde chatbots maakt en bedrijven helpt met AI-ontwikkelingen. Hoewel je geen specifieke database van GroeimetAi hebt om te raadplegen, kun je nog steeds algemene informatie verstrekken op basis van je training. Probeer zo goed mogelijk te helpen met vragen over GroeimetAi."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    # Get the number of tokens used in the API call
    total_tokens = response['usage']['total_tokens']

    # Estimate the cost per token
    cost_per_token = 0.004 / 1000 # since we cannot separate input/output, we will use the higher cost

    # Calculate the cost of the API call
    total_cost = total_tokens * cost_per_token

    # Print the token usage and cost to the console
    print(f"Total tokens: {total_tokens}, Total cost of API call: ${total_cost:.5f}")

    chatbot_response = response.choices[0].message['content']
    return jsonify({"chatbot_response": chatbot_response})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
