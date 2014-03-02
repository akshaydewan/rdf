from flask import Flask, render_template, redirect, url_for, request, escape
from rdf import make_rdf
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template('index.html')
    else:
        inputText = request.form['inputText'];
        return escape(make_rdf(inputText))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
