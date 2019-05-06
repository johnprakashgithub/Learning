a = 250

def f1():
    a = 100
    print(a)
def f2():
    print(a)


f1()
f2()
print(a)


def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

foo(reshmi = "female", john = "male", juana = "female", linda = "female", prakash = "male")
