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


class Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    surname = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    course = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer)

    def __repr__(self):
        d = {}
        d['name'] = self.name
        d['surname'] = self.surname
        d['email'] = self.email
        d['course'] = self.course
        d['year'] = self.year
        return str(d)

@app.route('/students', methods=['POST', 'DELETE'])
@app.route('/students/<int:sid>', methods=['GET', 'POST', 'DELETE'])
def student(sid=-1):
    print(request)
    if request.method == "GET":
        res = Student.query.filter_by(id=sid)
        if not res:
            return "Not exist"
        return repr(res)
    elif request.method == "POST":
        if sid == -1: #auto increment
            student = Student(**request.form)
            db.session.add(student)
            db.session.commit()
            return render_template("index.html")
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
        return render_template("index.html")
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
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'create':
        db.drop_all()
        db.create_all()
    app.run()
