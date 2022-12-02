from flask import Flask, render_template, request, jsonify

import chatbotMLbased as chatbot
import MySQLdb
import datetime


# Creating ChatBot Instancep
app = Flask(__name__)
app.static_folder = 'static'


db = MySQLdb.connect(host="db-mysql-sgp1-73465-do-user-12035841-0.b.db.ondigitalocean.com", 
                    user="doadmin", 
                    passwd="AVNS_1GNQHAtlxYOkhNeywGX", 
                    db="filkombot",
                    port=25060,
                    ssl={'ca': 'ca-certificate.crt'})
    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    intent = chatbot.pred_class(userText)
    responses = str(chatbot.get_response(intent))
    return jsonify(
        status='success',
        responses=responses,
        intent=intent[0]
    )

@app.route("/send_log", methods=['POST'])
def send_log_to_database():
    pesan = request.form.get('pesan')
    jawaban = request.form.get('jawaban')
    intent = request.form.get('intent')
    now_date = datetime.datetime.now()
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO log_chatbot (pertanyaan, jawaban, tag, waktu) VALUES (%s, %s, %s, %s)", (pesan, jawaban, intent, now_date))
        db.commit()
        return jsonify(
            status='success'
        )
    except:
        db = MySQLdb.connect(host="db-mysql-sgp1-73465-do-user-12035841-0.b.db.ondigitalocean.com", 
                    user="doadmin", 
                    passwd="AVNS_1GNQHAtlxYOkhNeywGX", 
                    db="filkombot",
                    port=25060,
                    ssl={'ca': 'ca-certificate.crt'})
        cursor = db.cursor()
        cursor.execute("INSERT INTO log_chatbot (pertanyaan, jawaban, tag, waktu) VALUES (%s, %s, %s, %s)", (pesan, jawaban, intent, now_date))
        db.commit()
        return "error"
        return jsonify(
            status='error'
        )

if __name__ == "__app__":
    app.run()