import os
import pandas as pd
import numpy as np
import pandas as pd
import pymongo
import json
import pickle
# from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, request, redirect, url_for
from sklearn.svm import SVC
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    pwd = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route('/charge', methods=['POST', 'GET'])
def pay():
	return redirect(url_for('form'))

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,34)
    loaded_model = pickle.load(open('./model/model.pkl',"rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Class 1: Psoriasis'
        elif int(result)==2:
            prediction='Class 2: Seboreic Dermatitis'
        elif int(result)==3:
            prediction = 'Class 3: Lichen Planus'
        elif int(result)==4:
            prediction ="Class 4: pityriasis rosea"
        elif int(result)==5:
            prediction ="Class 5: Chronic Dermatitis"
        elif int(result)==6:
            prediction = "Class 6: Pityriasis Rubra Pilaris"
            
        return render_template("form.html",result=prediction)


# @app.route("/contact", methods = ['GET', 'POST'])
# def contact():
#     if(request.method == 'POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         pwd = request.form.get('pwd')
#         entry = Contact(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
#         db.session.add(entry)
#         db.session.commit()

#     return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


    

    


