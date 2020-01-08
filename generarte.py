#!/usr/bin/env python3

import pymysql
import random

db = pymysql.connect("localhost","root","123456","flask")
cursor = db.cursor()
population = [chr(i) for i in range(97, 97+26)]
courses = ['philosophy', 'medicine', 'Software engineering', 'Jurisprudence', 'economics']
def randStr(n):
    size = random.randint(3, n)
    li = random.choices(population, k = size)
    return ''.join(li)
    
for i in range(1000):
    name = randStr(10)
    sname = randStr(10)
    email = randStr(5)+"@test.com"
    course = random.choice(courses)
    year = random.randint(0,4)
    sql = """insert into Student(name, surname, email, course, year) 
        values ('{}', '{}', '{}', '{}', {})""".format(name, sname, email, course, year)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        break
db.close()
    

