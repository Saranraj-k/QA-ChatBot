import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
    create table STUDENT(
    Name VARCHAR(50),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT)
"""

cursor.execute(table_info)


cursor.execute("INSERT INTO STUDENT VALUES('John', 'DATA SCIENCE', 'A', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Jane', 'DATA ANALYTICS', 'B', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Doe', 'MACHINE LEARNING', 'A', 75)")

print("The inserted records are:")
cursor.execute("SELECT * FROM STUDENT")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()