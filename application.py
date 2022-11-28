from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('RFModel.pkl', 'rb'))
car = pd.read_csv('Concrete_Data.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    Cement = request.form.get('Cement')
    Blast_Furnace_Slag = request.form.get('Blast_Furnace_Slag')
    Fly_Ash = request.form.get('Fly_Ash')
    Superplasticizer = request.form.get('Superplasticizer')
    Age = request.form.get('Age')
    prediction = model.predict(pd.DataFrame(columns=['Cement', 'Blast_Furnace_Slag', 'Fly_Ash', 'Superplasticizer', 'Age'],
                                            data=np.array([Cement, Blast_Furnace_Slag, Fly_Ash, Superplasticizer, Age]).reshape(1, 5)))
    print(prediction)
    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run()
