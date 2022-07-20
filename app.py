from flask import Flask, render_template, request

# import chatbotMLbased as chatbot


# Creating ChatBot Instancep

app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     intent = chatbot.pred_class(userText)
#     return str(chatbot.get_response(intent))

if __name__ == "__app__":
    app.run()