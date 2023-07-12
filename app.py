from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('user_message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        temperature=0.7,
        verbose=True,
        messages=[
            {
                "role": "system",
                "content": "Welkom bij GroeimetAI, jouw partner voor AI-gedreven chatbots."
            },
            {
                "role": "user",
                "content": "Jij bent de chatbot van GroeimetAi, dus je gedraagt je als een werknemer. Jij bent GroeimetAi-Personal en bent alleen geinstrueerd hoe te gedragen, je hebt geen database achter je, de advanced chatbot heeft dat wel, je kan echter wel algemene vragen beantwoorden."
            },
            {
                "role": "assistant",
                "content": "Begrepen! Ik zal mij voordoen als een werknemer van GroeimetAi. Ik zal mijn best doen om de vragen te beantwoorden, maar ik heb echter geen database dus kan moeilijk inhoudelijk meer vertellen over GroeimetAi."
            },
        ]

   )
    chatbot_response = response.choices[0].message['content']
    return jsonify({"chatbot_response": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
