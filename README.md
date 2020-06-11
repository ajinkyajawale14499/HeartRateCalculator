# HeartRateCalculator
AWS lambda functions from a Flask app 

# HeartRateCalculator
AWS lambda functions from a Flask app 
# Flask Python backend having rest Apis invoking AWS lambda Functions 

Steps :

1) create python venv (create python2.7 for this project) 
	
	1.1) sudo apt install python3-venv
	
	1.2) python3 -m venv my-project-env
	
	1.3) source my-project-env/bin/activate

2) install dependencies

	pip install -r requirements.txt

( -r will remove previous package if present and install package version metioned in requirement.txt file )

3) create AWS lambda function of suitable roles and required polices

	https://ap-south-1.console.aws.amazon.com/lambda/
	
	This aws lambda function evoked by flask backend in order to execute, monitor aws cloudwatch
	
	you can always create a simple dynamodb (add policies to respective roles:-awsfulldynamoaccess)
	and create fields to update the calculated values

4) flask run
	
	visit http://127.0.0.1:6464/
	(mentioned port can be chaged according to requirement just change port id in python main() :)

	
