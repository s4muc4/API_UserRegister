from flask import Flask, request

from db import insertUser

import os

os.environ.get('PORT', 5000)

app = Flask("Teste")

print("Routes rodando... ")

@app.route("/", methods=["GET"])
def main():
	return {"message":"Hospedagem no Heroku 😎"}



@app.route("/main", methods=["GET"])
def helloWorld():
	return {"message":"Hospedagem no Heroku 😎"}

@app.route("/register/user",methods=["POST"])
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
	
	return response

app.run()