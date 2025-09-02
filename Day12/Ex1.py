import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)")

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        print("Student added.")
    elif choice == "2":
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

conn.close()
