i=1
while(i<=20):
    if(i%2!=0):
     print(i)
    i+=1

av_seats=8
while(av_seats>0):
    seat_book=int(input("enter no of seats u want to book: "))
    if(seat_book<=av_seats):
        print("your seat is booked")
        av_seats-=seat_book
        print(f"no of available seats{av_seats}")
print("all seats are booked") 


i=10
while i>=1:
    print(f"happy new year {i}")
    i-=1

#for loop

num=int(input("enter a number:"))
for i in range(1,11):

    print(f"{num}X{i}={num*i}")



for i in range(1,6):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print()

    

cities=["mysuru","mandya","maddur","banglore"]
for i in cities:
    if i=="maddur":
        continue
    print(i)


#enumerate
cities=("mysuru","mandya","maddur","banglore")
for index,city in enumerate(cities):
    print(index,city)


cities = ("mysuru", "mandya", "maddur", "banglore")
for i in range(len(cities)):
    print(i, cities[i])

#multiples of 3
for i in range(31):
    if(i%3==0):
        print(i)


#Sum of First 10 Numbers:
sum=0
for i in range(1,11):
    sum+=i  #or sum=sum+i
            #i+=1
print(sum)

#Print Your Name Letter by Letter:
name=input("enter your name: ")
for letter in name:
    print(letter)
     

#Count Vowels in a String:
str=input("enter a string: ")
count=0
for letter in str:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U':
       count+=1
print(count)

#or

str=input("enter a string: ")
vowels="aeiouAEIOU"
count=0
for letter in str:
    if letter in vowels:
        count+=1
print(count)

#looping through lists

#Sum of all numbers in a list
list=[1,2,3,4,5]
print(sum(list))  #using built in method sum()


list=[10,20,30,40,50]
sum=0
for i in list:
    sum+=i
print(sum)

#Doubling each number in a list

l1=[2,4,6,8]
l2=[]
for num in l1:
    l2.append(num*2)  #correct method
print(l2)
