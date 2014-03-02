"""
    Reality Distortion Field. (Web Interface)
    A python module to distort a sentence as it would be spoken by 
    a certain sales executive.
    Copyright (C) 2014. Akshay Dewan <akudewan@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
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
