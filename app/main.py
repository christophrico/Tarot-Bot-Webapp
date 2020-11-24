import json
import os

from flask import Flask, redirect, render_template, request, session
from flask_dropzone import Dropzone

import image_handler as ih
import firestore_handler as fh


app = Flask(__name__)
# Flask-Dropzone config:
app.config.update(
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
)
dropzone = Dropzone(app)



"""
Home page with dropzone to upload photo for prediction
"""
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


"""
Handle a request to make a prediction from an uploaded photo
by Vision AutoML API and Firestore to store the prediction
"""
@app.route('/request-prediction', methods=['POST'])
def predict():
    app.logger.info("Requesting prediction from model")
    f = request.files['file']
    card, score = ih.request_prediction(file=f)

    #store the prediction in firestore to be viewed in homepage
    app.logger.info("Storing prediction in firestore")
    app.logger.info("Card: {} Score: {}".format(card, score))
    fh.update_database(card, score)
    return redirect('', 204)


"""
Display a list of all the previous predictions in Firestore
"""
@app.route('/retrieve-predictions', methods=['GET'])
def get_predictions():
    prediction_list = fh.get_predictions()
    
    if len(prediction_list) != 0:
        return render_template("results.html",
                                most_recent=prediction_list[0],
                                predictions=prediction_list[1:],
                              )
    else:
        return render_template("noresults.html")


"""
Some basic error handling
"""
@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(debug=True)
