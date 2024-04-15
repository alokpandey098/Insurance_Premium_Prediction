from flask import Flask
from Insurance.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("We are testing our logging file")

    return "Welcome to Insurance Premium Prediction Project!"

if __name__ == "__main__":
    app.run(debug = True) # 5000