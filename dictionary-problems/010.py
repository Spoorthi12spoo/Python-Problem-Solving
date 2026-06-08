#010.Update a value inside a nested dictionary.

student={"name":"abc","subjects":["maths","science","social"],
         "subject":{
             "maths":80,
              "science":70,
              "social":60}
}
res=student["subject"]["maths"]=90  
print(student)

student={
    "name":"abc",
    "student_details":{
        "age":25,
        "marks":
            {
                "maths":60,
                "science":70,
                "english":55
            } 
         }
}
student["student_details"]["marks"]["english"]=80
print(student)

student["student_details"]["marks"].update({"science":65})
print(student)

