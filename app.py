import os
from flask import Flask, request
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

""" @app.route("/")
def hello():
    return "Hello from Python!" """

@app.route("/", methods=["GET"])
def helloWorld():
	return {"message":"Hospedagem no Herokuu 😎"}

@app.route("/teste")
def teste():
    return "Testando segunda rota :D  !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)