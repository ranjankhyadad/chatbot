### About
- This Flask app is a chatbot that outputs the response to a message as a string on the page
- The bot is trained on the given set of (message,response) pairs provided to us in a `.csv` file

#### Assumptions
- The `query.csv` file is placed in the same folder as `mybot.py` file
- The format in the csv file is correct 

#### Steps to use

- Install requirements using `pip install -r requirements.txt`. It is recommended that you use a `virtualenv`
- Run `python mybot.py` on your terminal
- Go to the url - http://localhost:5000//chatbot/api/v1/querySet/{message} where {message} should be replaced by the message to the bot
    - Sample message-  "Are you a kid?"
- The response by the bot is displayed on the same page as a string
    - Sample response- "Age doesn't really apply to me."
- The response is also printed on the terminal