from config import PORT, HOST, DEBUG
from flask import Flask, render_template, request
import bot_response_maker
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot/get")
def get_bot_response():

    userText = request.args.get('msg')

    bot_response = bot_response_maker.give_response(userText)

    return bot_response


if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host=HOST, port=int(PORT))
