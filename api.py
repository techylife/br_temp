from flask import Flask, jsonify, request
from mailing import qna_confirm_mail
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route('/sendmail/<mail>/<docid>',methods=['POST'])
# @cross_origin()
def sendmail(mail, docid):
    stat = qna_confirm_mail(str(mail), str(docid))
    if stat == 1:
        return jsonify({"success":1,"message":"Mail sent successfully."})

@app.route('/say/<text>', methods=['POST'])
def say(text):
    return jsonify({"success":1,"message":str(text)})

app.run(debug=True)