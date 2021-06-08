from flask import Flask, request

from db import insertUser

import os

app = Flask("Teste")
port = int(os.environ.get("PORT", 5000))




print("Routes rodando... ")
print(os.environ.get)


@app.route("/", methods=["GET"])
def helloWorld():
	return {"message":"Hospedagem no Herokuu 😎"}

""" @app.route("/register/user",methods=["POST"])
def userRegister():

	body= request.get_json()

	if("name" not in body):
		return responseGenerate(400,"Parameter name is mandatory!")
	
	if("email" not in body):
		return responseGenerate(400,"Parameter email is mandatory!")

	if("password" not in body):
		return responseGenerate(400,"Parameter password is mandatory!")

	user=  insertUser(body["name"],body["email"],body["password"])

	return responseGenerate(200,"User created", "user", user)

def responseGenerate(status, message, contentName=False,  content=False):
	response = {}
	response["status"]= status
	response["message"] = message

	if (contentName and content):
		response[contentName] = content
	
	return response """

app.run(host='0.0.0.0', port=port)