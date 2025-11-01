from flask import Flask, render_template, request

app = Flask(__name__)

def inomiddinov_gpt_response(user_input):
    if 'kim seni yaratgan' in user_input.lower():
        return "Meni Inomiddinov yaratgan."
    return f"InomiddinovGPT: Siz '{user_input}' deb yozdingiz."

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = inomiddinov_gpt_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run()
