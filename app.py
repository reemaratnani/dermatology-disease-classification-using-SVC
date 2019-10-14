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
# model = pickle.load(open('./model/model.pkl','rb'))


app = Flask(__name__)
# MONGO_URL = os.environ.get('MONGO_URI')
# if not MONGO_URL:
#     MONGO_URL = "mongodb://localhost:27017/gene_db" 

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

# @app.route('/result',methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         ery = request.form['erythema']
#         scal = request.form['scaling']
#         bor = request.form['borders']
#         itch = request.form['itching']
#         koe= request.form['koebner']
#         poly = request.form['polygonal']
#         foll = request.form['follicular']
#         oral = request.form['oral']
#         knee = request.form['knee']
#         scalp = request.form['scalp']
#         history = request.form['history']
#         mel = request.form['melanin']
#         eos = request.form["eosinophils"]
#         pnl = request.form["pnl"]
#         fib = request.form['fibro']
#         exo = request.form['exo']
#         acan = request.form['acan']
#         kera = request.form['kera']
#         para = request.form['para']
#         club = request.form['club']
#         elon = request.form['elon']
#         epi = request.form['epi']
#         pus = request.form['pus']
#         munro = request.form['munro']
#         focal = request.form['focal']
#         lay = request.form['layer']
#         basal = request.form['basal']
#         spon = request.form['spon']
#         saw = request.form['saw']
#         horn = request.form['horn']
#         peri = request.form['peri']
#         mono = request.form['mono']
#         band = request.form['band']
#         age = request.form['age']

#         data = ery +" "+ scal +" "+ bor +" "+ itch +" "+" "+koe+" "+poly+" "+foll+" "+oral+" "+knee+" "+scalp+" "+history+" "+ \
#             mel+" "+eos+" "+pnl+" "+fib+" "+exo+" "+acan+" "+kera+" "+para+" "+club+" "+elon+" "+epi+" "+pus+" "+munro+" "+focal+\
#             focal+" "+lay+" "+basal+" "+spon+" "+saw+" "+horn+" "+peri+" "+mono+" "+band+" "+age
#         # print(data)
#         data
#         data = [data]
#         prediction = model.predict(data)
#         prediction = prediction[0]
        
#         return render_template("signup.html",result=prediction)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/gene_variants")
# def plot_data():
#     data = mongo.db.gene_variants
#     output = []
#     for x in data.find():
#         output.append({'Class' : x['Class'],'Gene' : x['Gene'], 'Variation':x['Variation']})
#     return jsonify(output)

# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")
    

# @app.route("/api/variation", methods=['GET'])
# def get_api():
#     # return render_template("api.html")
#     api = mongo.db.gene_variants

#     output = []
#     for x in api.find():
#         output.append({'Gene' : x['Gene'], 'Variation' : x['Variation']})
    
#     return jsonify({'result': output})

# @app.route("/api/class", methods=['GET'])
# def get_class():
#     # return render_template("api.html")
#     api = mongo.db.text

#     output = []
#     for x in api.find():
#         output.append({'Gene' : x['Gene'], 'Variation': x['Variation'],'Class' : x['Class'], 'Text': x['Text']})
    
#     return jsonify({'result': output})

# @app.route("/api/geneData", methods=['GET'])
# def get_geneData():
#     # return render_template("api.html")
#     api = mongo.db.geneData

#     output = []
#     for x in api.find():
#         output.append({'Gene Symbol' : x['Gene Symbol'], 'Name' : x['Name'], 'Tumour Types(Somatic)' : x['Tumour Types(Somatic)'],
#         'Tissue Type' : x['Tissue Type'], 'Molecular Genetics':x['Molecular Genetics'], 'Role in Cancer': x['Role in Cancer']})
    
#     return jsonify({'result': output})

# @app.route("/api/geneData/<gene>")
# def get_gene(gene):
#     results = mongo.db.geneData.find({'Gene Symbol': gene})
#     output = []
#     for x in results:
#         output.append({'Gene Symbol' : x['Gene Symbol'], 'Name' : x['Name'], 'Tumour Types(Somatic)' : x['Tumour Types(Somatic)'],
#         'Tissue Type' : x['Tissue Type'], 'Molecular Genetics':x['Molecular Genetics'], 'Role in Cancer': x['Role in Cancer']})
    
#     return jsonify({'result': output})



# @app.route('/result',methods = ['POST'])
# def result():
#     if request.method == 'POST':
#         variation = request.form['variation']
#         gene = request.form['gene']
#         text = request.form['text']
#         data = text +" "+ gene +" "+ variation
#         # print(data)
#         data = [data]
#         prediction = model.predict(data)
#         prediction = prediction[0]
        
#         return render_template("result.html",prediction=prediction)
# if __name__ == "__main__":
#     app.run(debug=True)