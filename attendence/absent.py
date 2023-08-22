f1=open("C:\\Users\\user\\Desktop\\python_codes\\attendence\\data.txt")
f2=open("C:\\Users\\user\\Desktop\\python_codes\\attendence\\present.txt")
total_students=set()
present_student=set()
for line in f1:
    total_students.add(line.rstrip("\n"))
print(total_students)

for line in f2:
    present_student.add(line.rstrip("\n"))
print(present_student)

# absent_student=total_students-present_student
# print(absent_student)

absent_student=total_students.difference(present_student)
print(absent_student)

