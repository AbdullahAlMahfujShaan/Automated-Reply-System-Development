from flask import Flask, request, render_template
from chatbot import chat
from datetime import datetime
from datetime import date

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("portal.html")


today = date.today()
now = datetime.now()
user = 0
# current_time: str = now.strftime("%H:%M:%S")
filename = 'user' + str(user) + 'date' + str(today) + '.txt'
f = open(filename, "a+")
# f= open(filename,"a")
f.write("Chat Started at : {0}".format(str(now.strftime("%H:%M:%S")))+'\n\n\n\n')
f.close()

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")

    f = open(filename, "a+")
    f.write('Anonymous User:' + userText + '\n\n' + 'NSUBOT: ' + str(chat(userText)) + '\n\n')
    f.close()
    return "Virtual-Assistant: " + str(chat(userText))


if __name__ == "__main__":
    app.run(debug=True)
