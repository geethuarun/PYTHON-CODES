# Question5


class Student:
    def _init_(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

class Teacher:
    def _init_(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name

    def assign_course(self, course):
        course.set_teacher(self)

class Course:
    def _init_(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = None
        self.students = []

    def set_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def display_details(self):
        teacher_name = self.teacher.name if self.teacher else "Not assigned"
        student_names = [student.name for student in self.students]
        
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Teacher: {teacher_name}")
        print(f"Enrolled Students: {', '.join(student_names)}")

# Creating instances of the classes
student1 = Student(1,"Alice")
student2 = Student(2,"Bob")

teacher1=Teacher(101,"Ms. Smith")
teacher2=Teacher(102,"Mr. Johnson")

course1 = Course(201, "Mathematics")
course2 = Course(202, "History")



# Enrolling students and assigning teachers
student1.enroll(course1)
student2.enroll(course2)

teacher1.assign_course(course1)
teacher2.assign_course(course2)

# Displaying course details
course1.display_details()
print("\n")
course2.display_details()