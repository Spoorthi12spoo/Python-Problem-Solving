#012.Remove items from a dictionary {1:10, 2:20, 3:30, 4:40} where the value is greater than 20 using dictionary comprehension.

D={1:10, 2:20, 3:30, 4:40} 
D1={key:value for key,value in D.items() if value<=20}
print(D1)
