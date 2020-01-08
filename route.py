#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sys
from config import app, db 
from modle import Student

@app.route('/students', methods=['GET', 'POST', 'DELETE'])
@app.route('/students/<int:sid>', methods=['GET', 'POST', 'DELETE'])
def student(sid=-1):
    if request.method == "GET":
        if sid == -1:
            sid = request.args.get("id")
        res = Student.query.filter_by(id=sid).first()
        if not res:
            return render_template("404.html", id=sid)
        return render_template("show.html", id=sid, info=res)
    elif request.method == "POST":
        if sid == -1: #auto increment
            student = Student(**request.form)
            db.session.add(student)
            db.session.commit()
            return render_template("success.html")
        stu = Student.query.filter_by(id=sid)
        if not stu:
            #update
            for key, value in request.form.items():
                setattr(stu, key, value)
        else:
            request.form['id'] = sid
            student = Student(**request.form)
            db.session.add(student)
            db.session.commit()
        return render_template("success.html")
    else:
        if sid == -1:
            sid = request.form['id']
        stu = Student.query.get(id=sid)
        if not stu:
            db.session.delete(stu)
            db.session.commit()
            return render_template("index.html")
        else:
            return "Not exist"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def add():
    return render_template('input.html')
