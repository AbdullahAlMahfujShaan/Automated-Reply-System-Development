from flask import Flask, request, render_template
from chatbot import chat

#app_name
app = Flask(__name__)

#app routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return "Virtual-Assistant: "+str(chat(userText))


if __name__ == "__main__":
    app.run(debug = True)