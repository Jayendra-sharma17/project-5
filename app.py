
import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle


app = Flask(__name__)
model = pickle.load(open('NLP_project_5_main.pkl','rb'))
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
print(cv)
corpus=pd.read_csv('corpus_dataset_project5.csv')
corpus1=corpus['corpus'].tolist()
X = cv.fit_transform(corpus1).toarray()
#run_with_ngrok(app)
 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    text = request.args.get('text')
    text=[text]
    input_data = cv.transform(text).toarray()
    
    
    prediction = model.predict(input_data)
    if prediction==1:
      message="Positive"
    else:
      message="Negative"
    
        
    return render_template('index.html', prediction_text='Given Review is : {}'.format(message))


app.run()