from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/fbcode.html')


if __name__ == '__main__':
    app.run(debug=True)