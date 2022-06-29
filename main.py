from flask import Flask, render_template, request

#from chatbot import chatbot
import os

import chatbotMLbased
import os

# Creating ChatBot Instancep

app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    intent = chatbotMLbased.pred_class(userText)
    return str(chatbotMLbased.get_response(intent))


if __name__ == "__main__":
    app.run()