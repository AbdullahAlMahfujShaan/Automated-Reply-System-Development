from flask import Flask, request, render_template
from chatbot import chat

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("portal.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return "Virtual-Assistant: "+str(chat(userText))


if __name__ == "__main__":
    app.run(debug = True)