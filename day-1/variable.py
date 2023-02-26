a = input("a: ")  # input 3
b = input("b: ")  # input 5

c = a
a = b
b = c

print("a: " + a)  # expected output 5
print("b: " + b)  # expected output 3
