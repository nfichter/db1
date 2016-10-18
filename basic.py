import sqlite3

db = sqlite3.connect("deez.db")
c = db.cursor()

c.execute("SELECT name,mark,courses.id FROM courses,peeps WHERE courses.id = peeps.id")

d = {}

for row in c.fetchall():
    grades = []
    d[row[2]] = [[row[0],row[2]],grades]
