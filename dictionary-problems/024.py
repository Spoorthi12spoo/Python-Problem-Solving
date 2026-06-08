#024.From a dictionary of student marks, print only students who scored above 80.

scores={'A':85, 'B':72, 'C':91}
for stud,score in scores.items():
    if score>80:
        print(stud,score)
