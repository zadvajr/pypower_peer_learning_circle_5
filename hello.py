# def hello():
#     print("Hello world")

# hello()

# def sum(a, b) -> int:
#     return a + b

# total = sum(5,19)

# print(total)
# print(type(total))

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

total = sum(4)
print(total)