# question 1
print(len("95637+12"))

# question 2
score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")


# question 4
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)


result = outer_function(5, 10)
print(result)


# question 8
def foo(a, b=4, c=6):
    print(a, b, c)


foo(20, c=12)


# question 9
def all_board(a, *arg, **kw):
    print(a, arg, kw)


all_board(4, 7, 3, 0, x=10, y=64)

# question 10
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
