import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="8081",
    user="root",
    passwd="mindfire",
    database="testdb"
)

mycursor = mydb.cursor()

"""Creating Database and Table"""

# mycursor.execute("CREATE DATABASE testdb")
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

"""Populating Database and Table"""

# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Bob", 12),
#            ("Amanda", 32),
#            ("Jacob", 21),
#            ("Avi", 28),
#            ("Michelle", 17),]
#
# mycursor.executemany(sqlFormula, students)
#
# mydb.commit()

""" Selecting and Getting Data"""

# mycursor.execute("SELECT * FROM students")
#
# # fetches data from last executed statement
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)

# fetches just one entry from last executed statement
# myresult = mycursor.fetchone()

"""Query Conditions and WHERE and Wildcards"""

# sql = "SELECT * FROM students WHERE name LIKE '%ac%'"

"""Updating Entries And Limiting Queries"""

# sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

# mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

"""Ordering Queries and Results"""

# sql = "SELECT * FROM students ORDER BY name DESC"

"""Deleting Entries and Dropping Tables"""

# sql = "DELETE FROM students WHERE name = 'Mike'"
# sql = "DROP TABLE IF EXISTS students"
# mycursor.execute(sql)
# mydb.commit()
