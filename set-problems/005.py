#005.Remove an element using remove() and discard() — explain difference.

S={1,2,4,5,6}
S.remove(5)  #remove raises KeyError if element not found
print(S)

S.discard(7)  #discard doesn't shows any  error if element not found
print(S)
