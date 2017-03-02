import json
import sqlite3


conn = sqlite3.connect('members_db.db')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS members;

CREATE TABLE IF NOT EXISTS users (
	id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	name    TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS courses (
	id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	name    TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS members (
    user_id INTEGER NOT NULL,
    course_id   INTEGER NOT NULL,
    role    INTEGER NOT NULL,
    PRIMARY KEY (user_id, course_id)
)''')

json_fp = open("roster_data.json")              #open the file and create a file pointer
obj = json.load(json_fp)                        #load the JSON to an object

for entry in obj:

    name = entry[0]
    course = entry[1]
    role = entry[2]

    #print "Name is: " + name
    #print "Course is: " + course

    cur.execute("INSERT OR IGNORE INTO users (name) VALUES ( ? )", (name,))
    user_id = cur.execute("SELECT id FROM users WHERE name = ?", (name,)).fetchone()[0]
    #print "user_id is:" + str(user_id)

    cur.execute("INSERT OR IGNORE INTO courses (name) VALUES ( ? )", (course,))
    course_id = cur.execute("SELECT id FROM courses WHERE name = ?", (course,)).fetchone()[0]
    #print "course_id is:" + str(course_id)

    cur.execute("INSERT OR IGNORE INTO members (user_id, course_id, role) VALUES (? , ? , ?)", (user_id, course_id, role))

    print "*************\n Now we are constructing....\n"
    results = cur.execute('''
    SELECT users.name AS Username, courses.name AS Title, members.role AS Role
    FROM members
    JOIN users ON users.id=members.user_id
    JOIN courses ON members.course_id=courses.id
    ORDER BY Username
    ''')

    entry = results.fetchone()

    while entry:
        print "******"
        print entry[0]
        print entry[1]
        print entry[2]
        print "\n"
        entry = results.fetchone()

conn.commit()

conn.close()
