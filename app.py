from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load(open('file.sav', 'rb'))
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)
@app.route('/about',methods=['POST','GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact',methods=['POST','GET','POST'])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
