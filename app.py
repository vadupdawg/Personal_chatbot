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
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": "Welkom bij GroeimetAI, jouw partner voor AI-gedreven chatbots. Hoe kan ik je helpen?"
            },
            {
                "role": "user",
                "content": "Jij bent de chatbot voor GroeimetAi, je probeert ook met de klant te mee te denken wat zij nodig hebben, we bieden vijf service levels: 1. Personal, 2. Advanced, 3. Professional, 4. Startup en 5. Enterprise. vanaf de Advanced chatbot krijgt de chatbot lange termijn geheugen die deze kan gebruiken om klanten of bezoekers van de website beter te informeren."
            },
            {
                "role": "assistant",
                "content": "Begrepen! Ik zal informatie verstrekken over onze chatbot-oplossingen, de verschillende service levels en hoe ze jouw bedrijf kunnen helpen. Voor complexe vragen zal ik voorstellen om een gesprek te starten. Laat me weten over welk soort bedrijf je informatie wilt, zodat ik relevante voorbeelden kan geven met GroeimetAi's slimme AI-chatbot oplossing die gebaseerd kunnen zijn op data uit jouw bedrijf, dit is echter wel een Advanced Service Level feature."
            },
        ]

   )
    chatbot_response = response.choices[0].message['content']
    return jsonify({"chatbot_response": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
