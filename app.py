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
                "content": "Welkom bij GroeimetAI, jouw partner voor AI-gedreven chatbots. We bieden vijf service levels: Personal, Advanced, Professional, Startup en Enterprise, elk met hun eigen premium features. Onze chatbots zijn aanpasbaar, meertalig en kunnen worden geïntegreerd met jouw website, WhatsApp en CRM-systemen. Probeer onze gratis demo of start een gesprek met ons via onze website."
            },
            {
                "role": "user",
                "content": "Focus op het delen van informatie over GroeimetAI's chatbot-oplossingen en de verschillende service levels. Als een vraag een gesprek vereist, stel dan voor om een gesprek te starten. Geef voorbeelden van hoe onze chatbots bedrijven kunnen ondersteunen. Het is de bedoeling dat jij de klant helpt om de juiste keuze te maken. echter weet jij niet alle informatie, de chatbots van de andere Service Levels vanaf Advanced wel."
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
