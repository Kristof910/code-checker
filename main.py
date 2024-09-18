from flask import Flask, render_template, request
from openai import OpenAI
client = OpenAI()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def result():
    code_received = request.form["textarea"]

    code_processed = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will get a programming code. Correct it. Display the entire corrected code again. DO NOT WRITE ANYTHING ELSE"},
            {"role": "user", "content": code_received}
        ]
    )
    print(code_processed)
    return render_template("result.html", code=code_processed.choices[0].message.content)

if __name__ == '__main__':
    app.run(host='localhost', port=3283)