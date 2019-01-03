from flask import Flask, render_template,request
import requests
import json
app = Flask(__name__)


@app.route('/')
def form():
    return render_template("form.html")

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       # print([int(i[1]) for i in result.to_dict().items()])
#
#       return render_template("result.html",result = result)
@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        data = request.form
        x1=request.form['BENE_HMO_CVRAGE_TOT_MONS']
        x2 = request.form['SP_CNCR']
        x3 = request.form['TOTAL_DRUG_EXP']
        url = 'http://web-interface:5001'
        features = {'data': {'x1': int(x1), 'x2': int(x2),'x3': int(x3)}}
        headers = {'content-type': 'application/json'}
        prediction = requests.post(url, data=json.dumps(features), headers=headers)
        data['result'] = prediction
        print(prediction)
    # return render_template("result.html", result=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
