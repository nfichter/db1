import csv
import sqlite3

fial="deez.db"

db = sqlite3.connect(fial)
c = db.cursor()

c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)
for k in d:
    c.execute("INSERT INTO peeps VALUES (\""+k['name']+"\",\""+k['age']+"\",\""+k['id']+"\")")

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

fObj2 = open("courses.csv")
d2=csv.DictReader(fObj2)
for k in d2:
    c.execute("INSERT INTO courses VALUES (\""+k['code']+"\",\""+k['mark']+"\",\""+k['id']+"\")")

db.commit()
db.close()
