from flask import Flask, render_template,request
import requests
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
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        data = request.form
        result = requests.post('http://web-interface:5001/result', json=data.to_dict())
        data['result'] = result
        print(result)
    return render_template("result.html", result=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
