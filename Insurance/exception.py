from flask import Flask
from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception("we are testing our Exception file") # Error
    except Exception as e:
        ML = InsuranceException(e, sys)
        logging.info(ML.error_message)
        
        logging.info("We are testing our logging file")

        return "Welcome to Insurance Premium Prediction Project!"

if __name__ == "__main__":
    app.run(debug = True) # 5000