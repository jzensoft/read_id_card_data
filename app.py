from flask import Flask

from read_data import reader

app = Flask(__name__)


@app.route('/')
def hello():
    return reader('assets/images/id_card.jpg', 'th', 0, False)


if __name__ == "__main__":
    app.run(debug=True)
