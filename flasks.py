from flask import Flask
app = Flask(__name__) #flask 인스턴스화 시킴
@app.route("/")

def helloworld():
    str = "Hello World! Raspberry Jang!!!"
    return str

app.run(host='0.0.0.0', port='8000') #host = ip