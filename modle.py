#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sys
from config import db

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
