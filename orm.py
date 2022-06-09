import sqlite3
from prog import Student


class StudentMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id):
        statement = 'SELECT id, name, purse, grade FROM student WHERE id=?'

        self.cursor.execute(statement, (id))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise DatabaseError(f'record with id={id} not found')

    def insert(self, student):
        statement = 'INSERT INTO Student(name, purse, grade, age) VALUES (?, ?, ?, ?)'
        self.cursor.execute(statement, (student.name, student.purse, student.grade, student.age))
        try:
            self.connection.commit()
        except Exception as e:
            raise DatabaseError(e.args)

    def update(self, student):
        statement = "UPDATE student SET age=? WHERE name=?"
        self.cursor.execute(statement, (student.name, student.age))
        try:
            self.connection.commit()
        except Exception as e:
            raise DatabaseError(e.args)


    def delete(self, student):
        statement = "DELETE FROM student WHERE name=?"
        self.cursor.execute(statement, (student.name, ))
        try:
            self.connection.commit()
        except Exception as e:
            raise DatabaseError(e.args)


conn = sqlite3.connect('education.db')
student_mapper = StudentMapper(conn)
student = student_mapper.insert(Student('Grigory Zaharov', 15000, 'junior', age=22))
student1 = student_mapper.find_by_id(1)
print(student1.__dict__)
