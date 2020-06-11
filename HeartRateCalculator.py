# heart rate calculator based on age of the user
from flask import Flask,jsonify,request,render_template
import boto3
import json
import logging
from conf import credentials as conf

#create lambda client
client = boto3.client('lambda',
                      region_name = conf.region,
                      aws_access_key_id = conf.aws_access_key_id,
                      aws_secret_access_key = conf.aws_secret_access_key)

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)

@app.route("/",methods = ['GET' , 'POST'])
@app.route("/calculate_heart_range",methods=['GET', 'POST'])
def calculate_heart_range():
    if request.method == 'GET':
        #return form
        return render_template('sample_lambda.html')
    if request.method == 'POST':
        #return range
        age = int(request.form.get('age'))
        payload = {
            "age" : age
        }
        #invoke a lambda function to calculate the max heart rate
        result = client.invoke(FunctionName= conf.lambda_function_name,
                               InvocationType = 'RequestResponse',
                               Payload = json.dumps(payload))
        range = result['Payload'].read()
        api_response = json.dumps(range)
        return jsonify(api_response)

#driver function
if __name__=='__main__':
    app.run(host='127.0.0.1', port=6464, debug=True)

