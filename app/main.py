import os
from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import image_handler as ih

app = Flask(__name__)


app.config.update(
    #UPLOADED_PATH=os.path.join(./, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)
dropzone = Dropzone(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predicting', methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']

        prediction = ih.get_prediction(file=f)
        print(prediction)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, use_reloader=True)
