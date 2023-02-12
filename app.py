import os.path

from flask import Flask, request, abort

from src import detector
from utils.Utils import allowed_file

UPLOAD_FOLDER = 'assets/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return abort(400, "No selected file.")
        image = request.files['image']
        if image.filename == '':
            return abort(400, "No selected file.")
        if image and allowed_file(image.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(path)
            return detector.detect_image(path, 'th', 0, False)
        else:
            return abort(400, "Incorrect file type.")
    except BaseException as e:
        abort(400, str(e))


if __name__ == "__main__":
    app.run(debug=True)
