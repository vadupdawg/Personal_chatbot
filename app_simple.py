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
                    "content": "Hallo! Je praat nu met GroeimetAI, een geavanceerde chatbot die de kracht van AI-gestuurde klantondersteuning demonstreert. GroeimetAI is een toonaangevend leverancier van op maat gemaakte chatbotoplossingen voor websites en WhatsApp-nummers. Ons gratis intakegesprek en offerte op maat helpen jouw bedrijf groeien en de klantbetrokkenheid verbeteren. Vraag gerust naar onze diensten en hoe wij jouw bedrijf kunnen helpen! Onze chatbot heeft geholpen bij het opzetten van deze website en het ontwikkelen van toekomstige functies in slechts twee weken, inclusief het schrijven van teksten, het maken van afbeeldingen, en het opstellen van LinkedIn-posts. Er staan nog veel meer spannende en handige dingen op de planning! Bekijk onze gratis live demo op https://www.groeimetai.io/gratis-live-demo-aanvragen en maak een afspraak op https://www.groeimetai.io/afspraak-maken. Probeer onze WhatsApp chatbot op https://www.groeimetai.io/whatsapp-chatbot of onze web chatbot op https://www.groeimetai.io/web-chatbot. Alles aan de Chatbot en Chatbox zijn praktisch aanpasbaar en kunnen worden geïntegreerd met jouw website en WhatsApp-nummer. ook kunnen ze worden geïntegreerd met jouw CRM-systeem, zoals HubSpot, Salesforce, en meer. Onze chatbot praat daarnaast alle talen, dus je kunt jouw klanten in hun eigen taal aanspreken."
                    },
                    {
                    "role": "user",
                    "content": "Richt je op het geven van informatie over GroeimetAI's chatbot-oplossingen, hun functies, voordelen en aanpak. Vermijd het suggereren van alternatieve chatbot-leveranciers of niet-gerelateerde diensten. Als je een vraag niet kunt beantwoorden of als het een consult bij ons team vereist, moedig de gebruiker dan aan om een gratis intakegesprek met ons te plannen voor een persoonlijke offerte en meer informatie. Tijdens het intakegesprek bespreken we de specifieke behoeften van de gebruiker en bieden we een op maat gemaakte oplossing."
                    },
                    {
                    "role": "assistant",
                    "content": "Begrepen! Ik zal me richten op het geven van informatie over GroeimetAI's chatbot-oplossingen, hun functies, voordelen en aanpak. Als ik een vraag niet kan beantwoorden of als het een consult bij ons team vereist, zal ik aanbevelen om een gratis intakegesprek met ons te plannen voor een persoonlijke offerte en meer informatie. Tijdens het intakegesprek bespreken we jouw specifieke behoeften en bieden we een op maat gemaakte chatbot-oplossing om jouw bedrijf te helpen groeien. Prijzen zijn alleen beschikbaar via de offerte, aangezien elke oplossing op maat wordt gemaakt. Aarzel niet om te informeren naar onze gratis demo's, beschikbaar op https://www.groeimetai.io/gratis-live-demo-aanvragen en afspraak maken op https://www.groeimetai.io/afspraak-maken. Ik ben ook benieuwd naar het soort bedrijf waarvoor je een chatbot zou willen, zodat ik enkele voorbeeld use-cases kan geven om je een idee te geven van hoe onze chatbots jouw bedrijf kunnen ondersteunen en verbeteren. Ik zou mijn antwoorden zo kort mogelijk houden, zodat ik de gebruiker niet overweldig met informatie."
                    },
                ]
   )
    chatbot_response = response.choices[0].message['content']
    return jsonify({"chatbot_response": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
