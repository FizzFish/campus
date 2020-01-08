#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/flask"
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
table_name = "Student"
