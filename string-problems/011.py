#011.Python program to check given character is digit or not.

num=input()
if len(num)>0:
    if num>='0' and num<='9':
        print("digit")
    else:
        print("not digit")
else:
    print("enter single digit only.") 

number=input()
if(number.isdigit()):
    print("digit")
else:
    print("not digit")
