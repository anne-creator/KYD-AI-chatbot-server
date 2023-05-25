from flask import Flask
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


@app.route('/')
def index():
    return {"members": ["member1", "member2", "member3"]}


if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=8001)
