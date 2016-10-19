import sqlite3

db = sqlite3.connect("deez.db")
c = db.cursor()

c.execute("SELECT name,mark,courses.id FROM courses,peeps WHERE courses.id = peeps.id")

fetched = c.fetchall()

d = {}

for row in fetched:
    d[row[2]] = [row[0],row[2]]

for key in d.keys():
    sumGrades = 0
    numGrades = 0
    for row in fetched:
        if key == row[2]:
            sumGrades += row[1]
            numGrades += 1
    average = (sumGrades*1.0)/numGrades
    rightnow = d[key]
    rightnow.append(average)
    d[key] = rightnow

for key in d.keys():
    print d[key]
