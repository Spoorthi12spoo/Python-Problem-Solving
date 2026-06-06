#029 Access a deeply nested element
# Access the element 4
t = (1, (2, (3, (4, 5))))
E = 4

def access_element(t, E):
    for i in t:
        if isinstance(i, tuple):
            if access_element(i, E):
                return True
        elif i == E:
            print("element found")
            return True
    return False
  if not access_element(t, E):
    print("element not found")
