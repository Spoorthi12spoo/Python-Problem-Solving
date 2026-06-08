#004.Merge two dictionaries using both update() and | operator.

student={"name":"abc","branch":"CSE","year":2}
student1={"college":"xyz"}
student.update(student1)
res=student|student1
print(student)
print(res)
