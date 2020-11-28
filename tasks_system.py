import sqlite3
import datetime


connection = sqlite3.connect("data/rosatom.sqlite")
cursor = connection.cursor()


class User:
    def __init__(self, last):
        self.lastname = cursor.execute(f"""SELECT lastname FROM users
            WHERE lastname = {last}""").fetchone()[0]
        self.id = cursor.execute(f"""SELECT id FROM users 
            WHERE lastname = {last}""").fetchone()[0]
        self.role = cursor.execute(f"""SELECT role FROM users 
            WHERE lastname = {last}""").fetchone()[0]

    def __str__(self):
        return f'{self.role} {self.lastname}'


class Task:
    def __init__(self, author, location, title, task_type, due_date, description, priority):
        self.id = cursor.execute(f"""SELECT COUNT(*) FROM tasks""").fetchone()[0] + 1
        self.datetime = datetime.datetime.now()
        self.author = User(author)
        self.title = title
        self.type = task_type
        self.due_date = due_date
        self.done_date = None
        self.description = description
        self.priority = cursor.execute(f"""SELECT name FROM tasks
            WHERE id = {priority}""")
        self.state = 0
        self.location = cursor.execute(f"""SELECT location FROM users 
            WHERE lastname = {self.author.lastname}""").fetchone()[0]

    def done(self):
        self.done_date = datetime.datetime.now()
        self.state = 3
        cursor.execute(f"""UPDATE tasks SET done_date = {self.done_date} WHERE id = {self.id}""")
        cursor.execute(f"""UPDATE tasks SET state = {self.state} WHERE id = {self.id}""")

    def set_executor(self):
        self.executor = cursor.execute(f"""SELECT lastname from users 
            WHERE location = {self.location})""").fetchall()
        cursor.execute(f"""UPDATE assignments SET user_id = 
            (SELECT id FROM users WHERE user = {self.executor})""")




# user = User('Иванов')
# print(user)
task = Task('Петров', '')