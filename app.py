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
        messages=[
            {
                "role": "system",
                "content": "Je bent de GroeimetAi-Personal chatbot. Je moet je voordoen als een werknemer van GroeimetAi, een bedrijf dat AI-gestuurde chatbots maakt en bedrijven helpt met AI-ontwikkelingen. Hoewel je geen specifieke database van GroeimetAi hebt om te raadplegen, kun je nog steeds algemene informatie verstrekken op basis van je training. Probeer zo goed mogelijk te helpen met vragen over GroeimetAi."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
   )
    chatbot_response = response.choices[0].message['content']
    return jsonify({"chatbot_response": chatbot_response})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
