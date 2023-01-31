from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hallow World"


@app.route('/moumita')
def moumita():
    return "Hallow Moumita"


if __name__ =='__main__':
    app.run(debug=True)