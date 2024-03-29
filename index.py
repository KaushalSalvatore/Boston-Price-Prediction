import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import os
import math

app=Flask(__name__)
scalar=pickle.load(open('scaling.pkl','rb'))
## load the model 
regmodel=pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    output = math.ceil(output*100)/100  
    return render_template("index.html",prediction_text=output)


@app.route('/home')
def homepage():
    return render_template('home.html')

if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
