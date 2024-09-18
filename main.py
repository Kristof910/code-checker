from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def result():
    code = request.form["textarea"]
    print(code)
    return render_template("result.html", code=code)

if __name__ == '__main__':
    app.run(host='localhost', port=3283)