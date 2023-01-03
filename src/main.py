from Chatbot.api import app

if __name__ == "__main__":
    app.run(debug=False, port=3500)
    # user_question = "What is the capital of USA?"
    # reply = chatbot.get_reply(user_message=user_question)
    # print(reply)