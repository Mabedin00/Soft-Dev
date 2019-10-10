# Mohidul Abedin; Brian Moses; Team Mo^2

# SoftDev1 pd2

# K17 -- No Trouble

# 2019-10-11

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #opens the file MUST RUN db_builder first
c = db.cursor()

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"

foo = c.execute(q)
