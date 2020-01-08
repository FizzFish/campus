#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sys
from config import app, db 
from route import student, index

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'create':
        db.drop_all()
        db.create_all()
    app.run()
