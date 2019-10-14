import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="stanley123",
        database = "testdb"
    )

cursor = mydb.cursor()
sql_1 = "DROP TABLE IF EXISTS students"
cursor.execute(sql_1)
sql_2 = "CREATE TABLE students (name VARCHAR(100), age INTEGER(3))"
cursor.execute(sql_2)

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

student1 = ("Stanley", 30)
students = [("John", 11), ("Smith", 9), ("Bob", 8), ("Peter", 12), ("Johnny", 9)]
cursor.execute(sqlFormula, student1)
cursor.executemany(sqlFormula, students)

sql_3 = "INSERT INTO students VALUES ('Catherine', 6)"
cursor.execute(sql_3)

mydb.commit()

# cursor.execute("SELECT age FROM students")
# results = cursor.fetchone()
# print("Age: {}".format(results))

# for row in results:
#     print("Age: {}".format(row[0]))

# sql = "SELECT * FROM students WHERE age<30"

# sql = "SELECT * FROM students WHERE name LIKE 'John%'"

# sql = "SELECT * FROM students WHERE name LIKE %s"

# sql = "SELECT * FROM students ORDER BY age DESC"

# sql = "UPDATE students SET age=%s WHERE name=%s"

# sql = "SELECT * FROM students LIMIT 3"

# skip the first two rows
# sql = "SELECT * FROM students LIMIT 3 OFFSET 2"

# sql = "SELECT * FROM students ORDER BY name DESC LIMIT 3 OFFSET 3"

# sql = "INSERT INTO students (name, age) VALUES ('Stanley', 30)"

# sql = "DELETE FROM students WHERE name=%s"
# must use a tuple - (something, )
# cursor.execute(sql, ("Stanley",))
# cursor.execute(sql)
# cursor.execute(sql, ("40", "Stanley"))
# result = cursor.fetchall()
# mydb.commit()
# for re in result:
#     print("result: {}".format(re))