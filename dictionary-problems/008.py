#008.Remove a key from a dictionary using pop() and using del.

student={"name":"abc","age":8,"branch":"CSE"}
student.pop("name")
print(student)

del student["age"]      #del student deletes entire dictionary if u try to print it gives name student not defined
print(student)
