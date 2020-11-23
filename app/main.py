import json
import os

from flask import Flask, redirect, render_template, request, session
from flask_dropzone import Dropzone

import image_handler as ih
import firebase_handler as fh

app = Flask(__name__)
# Flask-Dropzone config:
app.config.update(
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)
dropzone = Dropzone(app)


"""
Home page
"""
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


"""
Handle a request to make a prediction from an uploaded photo
by using AutoML API and firestore to store the prediction
"""
@app.route('/request-prediction', methods=['POST'])
def predict():
    print("Requesting prediction...")
    f = request.files['file']
    prediction = ih.request_prediction(file=f)

    #store the prediction in firestore to be viewed in homepage
    print("Storing prediction in Firestore...")
    fh.update_database(prediction)
    return redirect("/retrieve-predictions")


@app.route('/retrieve-predictions')
def get_predictions():
    prediction_list = fh.get_predictions()
    return render_template("results.html", predictions=prediction_list)



if __name__ == '__main__':
    app.run(debug=True)
