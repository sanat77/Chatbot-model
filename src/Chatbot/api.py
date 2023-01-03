from flask import Flask, request
from flask_cors import cross_origin
import os
import json
from dotenv import load_dotenv

from Chatbot.Chatbot import Chatbot

load_dotenv()
URL_PREFIX = os.getenv("URL_BASE_PREFIX")
app = Flask(__name__)

@app.route(f"/{URL_PREFIX}/bot-response", methods=["POST"])
@cross_origin()
def get_bot_response():
    body = request.json
    chatbot = Chatbot()
    user_message = ''
    # get the user message
    try:
        user_message = body['message']
    except:
        print("EXCEPTION: NO FIELD NAMED MESSAGE")
        return app.response_class(
            response="",
            status=400
        )
    
    bot_reply = ''
    try:
        bot_reply = chatbot.get_reply(user_message=user_message)
    except:
        print("EXCEPTION: AI MODEL CANNOT GET REPLY")
        return app.response_class(
            response="",
            status=400
        )

    response = app.response_class(
        response=bot_reply,
        status=200
    )
    return response