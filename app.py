import os
import pandas as pd
import numpy as np
import pandas as pd
import pymongo
import json
import pickle
# from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, request
from sklearn.svm import SVC

app = Flask(__name__)
# MONGO_URL = os.environ.get('MONGO_URI')
# app.config["MONGO_URI"] = MONGO_URL
# mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


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

if __name__ == "__main__":
    app.run(debug=True)


    

    


