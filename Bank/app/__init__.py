# init Module

from flask import Flask

app = Flask(__name__)

from Bank.app import userData
