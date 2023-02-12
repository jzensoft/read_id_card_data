import os.path

from flask import Flask, request, abort

import read_data

UPLOAD_FOLDER = 'assets/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return abort(400, "Please, select image")
        image = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)
        return read_data.reader(path, 'th', 0, False)
    except BaseException as e:
        abort(400, str(e))


if __name__ == "__main__":
    app.run(debug=True)
