# global variable
value = 10


def sample():
    # local variable
    value = 20
    print(value)


sample()
print(value)


def id(name, age):
    print(name, age)


id(name="sdfaf", age=23)
id("sfgjk", 45)
