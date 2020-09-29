# Imports
from flask import Flask, abort, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import urllib
import os
from dotenv import load_dotenv

app = Flask(__name__)

# parsing username and password to use in db URI
load_dotenv()
username = urllib.parse.quote_plus(os.getenv("username")).lower()
password = urllib.parse.quote_plus(os.getenv("password"))

# Create bot
bot = ChatBot('Octo',
               storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
               database_uri = "mongodb+srv://%s:%s@cluster0.8e22h.mongodb.net/mybot_conversations?retryWrites=true&w=majority" %(username, password)
)

# Create a trainer
trainer = ListTrainer(bot)

# Use csv file to train the bot
querySet = []

with open("query.csv", "r") as file:
    content = file.readlines()[1:]
    for line in content:
        line = line.split(",")
        querySet.append(line[0])
        querySet.append(line[1])

trainer.train(querySet) 

# Route to display all items in queryset
@app.route("/chatbot/api/v1/querySet/")
def get_all():
    with app.app_context():
        return jsonify(querySet)

# Main Route- fetch message from the url params and display the response of the bot as a string on webpage
@app.route("/chatbot/api/v1/querySet/<message>")
def get_response(message):
    response = bot.get_response(message)
    print(response)
    if len(message) == 0:
        abort(404)
    return str(response)
 
if __name__ == "__main__":
    app.run(debug=True)