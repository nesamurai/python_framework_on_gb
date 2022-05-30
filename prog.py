class Student():
    def __init__(self, name, purse, grade):
        self.name = name
        self.purse = purse
        self.grade = grade
        self.courses = []


class Course():
    def __init__(self, category, name, students=[], is_online=True, address=None):
        self.category = category
        self.name = name
        self.students = students
        self.is_online = is_online
        self.address = address
        self.free = True
        self.cost = None
        self.level = None



class CourseBuilder:
    def __init__(self, category=None, name=None, students=[], is_online=True, address=None):
        self.course = Course(category, name, students, is_online, address)

    def need_pay(self):
        self.course.free = True
        self.course.cost = 0

    def get_level(self):
        self.course.level = 'basic'

    def add_student(self, student):
        self.students.append(student)

    def create(self):
        return self.course


course_builder = CourseBuilder('programming', 'python')
course_builder.need_pay()
course_builder.get_level()
first_student = Student('Petr Popov', 20000, 'junior')
course_builder.add_student(first_student)
python_course = course_builder.create()
first_student.courses.append(python_course)
