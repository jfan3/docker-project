# from flask import *
# import findspark
# findspark.init()
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline,PipelineModel
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel
import requests
from flask import Flask, render_template,request,jsonify


app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def predict ():
   model = PipelineModel.load("models/pipeline_model")
   # response = requests.get('http://web-interface:5000')
   # data_dict = response.json().to_dict()
   data = request.get_json()['data']
   # data_temp = [int(i[1]) for i in data_dict.items()]
   data = spark.createDataFrame([list(data.values())], ["BENE_HMO_CVRAGE_TOT_MONS", "SP_CNCR", "TOTAL_DRUG_EXP"])
   result = model.transform(data).select("prediction").show()
   return jsonify({"prediction": result})

# @app.route('/', methods=['POST'])
# def predict():
#     data = request.get_json()['data']
#     feature = Vectors.dense(list(data.values()))
#     test_data = spark.createDataFrame([{"features": feature}])
#     predicted = model.transform(test_data)
#     val = predicted.collect()[0]["prediction"]
#     return jsonify({"prediction": val})

if __name__ == '__main__':
   spark = SparkSession.builder.getOrCreate()
   # print('HereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHereHere')

   app.run(debug=True, host='0.0.0.0', port='5001')




