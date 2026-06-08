#009. Create a nested dictionary of student details and print: * name * subjects* marks of one subject

student={"name":"abc","subjects":["maths","science","social"],
         "subject":{
             "maths":80,
              "science":70,
              "social":60}
}
print("name",student["name"])
