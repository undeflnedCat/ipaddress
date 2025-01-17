from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def ip():
    return request.remote_addr