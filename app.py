# Don't update this file, it's standard across all providers
from flask import Flask, request , abort , make_response, jsonify
import uuid
import requests
from provider import run
from threading import Thread

app = Flask(__name__)

@app.route('/')
def handle():

	args = request.args.to_dict()
	headers = request.headers

	if "webhook_url" in headers:
		webhook_url = headers["webhook_url"]
	else:
		abort(make_response(jsonify(message="Missing webhook URL"), 400))

	if "jwt" in headers:
		jwt = headers["jwt"]
	else:
		abort(make_response(jsonify(message="Missing JWT"), 400))

	if "target_address" in args:
		target_address = args["target_address"]
	else:
		abort(make_response(jsonify(message="Missing target address"), 400))

	requestId = uuid.uuid4().hex
	
	thread = Thread(target=runProvider, args=(webhook_url,jwt,target_address))
	thread.start()

	return jsonify(id=requestId, status="pending")

def runProvider(webhook_url,jwt,target_address):

	providerData = run(target_address)
	requests.post(webhook_url, json=providerData, headers={"jwt": jwt, "content-type": "application/json"})
	print("Provider finished")
