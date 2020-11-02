from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import image_handler as ih

app = Flask(__name__)


app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
    DROPZONE_REDIRECT_VIEW='predicting'  # set redirect view
)


dropzone = Dropzone(app)

@app.route('/', methods=['POST'])
def upload():
    f = request.files.get('file')
    prediction = ih.getPrediction(file=f)

    for result in prediction.payload:
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.classification.score))

    return render_template('index.html')


@app.route('/predicting')
def predicting():
    return render_template(index.html)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, use_reloader=True)
