class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}")

    def get_email(self):
        return self.__email

    def __repr__(self):
        return f"Person({self.id}, {self.name}, {self.__email})"


class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    def __repr__(self):
        return f"Student({self.id}, {self.name}, GPA={self.gpa})"


class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = []

    def assign_course(self, course):
        self.courses_teaching.append(course)

    def __repr__(self):
        return f"Professor({self.id}, {self.name}, Dept={self.department})"


s1 = Student(101, "Mohammed", "mohammed@example.com", "CS", 3.8)
s2 = Student(102, "Yousef", "yousef@example.com", "Math", 3.5)

p1 = Professor(201, "Dr. Ahmad", "ahmad@uni.com", "CS")

s1.enroll("CS101")
s2.enroll("Math201")
p1.assign_course("CS101")

s1.display_info()
print(s1.get_email())
print(s1.courses)


print(s1 < s2)

print(s1)  
print(p1)  