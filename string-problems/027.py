#027.Python program to print all non repeating character in string.

input_str=input()
res=''
freq_dict={}
for i in input_str:
    if i in freq_dict:
      freq_dict[i]+=1
    else:
       freq_dict[i]=1
                       
for char in input_str:
    if(freq_dict[char]==1):
        print(char,end="")
