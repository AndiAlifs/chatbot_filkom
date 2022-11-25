from flask import Flask, render_template, request

import chatbotMLbased as chatbot
import MySQLdb
import datetime

# establish database connection
db = MySQLdb.connect(host="db-mysql-sgp1-73465-do-user-12035841-0.b.db.ondigitalocean.com", 
                    user="doadmin", 
                    passwd="AVNS_1GNQHAtlxYOkhNeywGX", 
                    db="filkombot",
                    port=25060,
                    ssl={'ca': 'ca-certificate.crt'})

# Creating ChatBot Instancep
app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    intent = chatbot.pred_class(userText)
    return str(chatbot.get_response(intent))

@app.route("/send_log", methods=['POST'])
def send_log_to_database():
    pesan = request.form.get('pesan')
    jawaban = request.form.get('jawaban')
    now_date = datetime.datetime.now()
    cursor = db.cursor()
    cursor.execute("INSERT INTO log_chatbot (pertanyaan, jawaban, waktu) VALUES (%s, %s, %s)", (pesan, jawaban, now_date))
    db.commit()
    return "success"


if __name__ == "__app__":
    app.run()