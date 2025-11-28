args = 5

class A:
    def __init__(self, input):
        self.input = input

a = A(args)
print(a.input)

args = 8

print(a.input)