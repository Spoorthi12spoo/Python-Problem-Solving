#008.Find the second largest element in a list.

l = list(map(int, input("Enter numbers: ").split()))  
first_max = second_max = float('-inf')
for num in l:
    if num > first_max:
        second_max = first_max 
        first_max = num        
    elif num > second_max and num != first_max:
        second_max = num       
if second_max == float('-inf'):
    print("No second largest element")
else:
    print("Second largest element:", second_max)
