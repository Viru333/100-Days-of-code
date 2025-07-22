# import tkinter
#
# window = tkinter.Tk()
#
# window.title("My First GUI Program")
# window.minsize(width = 500, height = 300)

# Label

# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.pack() # to show on gui

# Setting default values for optional arguments inside a function header

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)

# def fun(a,b=3,c=5):
#     print(a, b, c)
#
#
# fun(1)
# fun(1,2)
# fun(1,2,3)
# fun(1,b=9)
# fun(1,c=0)

# UNLIMITED ARGUMENTS or POSITIONAL ARGUMENTS (*args)

# def add(*args): # args is a tuple
#     print(args[0])
#     sum_ = 0
#     for n in args:
#         sum_ += n
#     return sum_
#
#
# print(add(1,2,3,8439.439534))


# UNLIMITED KEYWORD ARGUMENTS (*kwargs) it's a dictionary

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

class Cars:

    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]
        self.model = kw.get("model") # if this key doesn't exits in the dict(kw) then it doesn't give error and return none
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# my_car = Cars(make="Nissan", model="GTR")
my_car = Cars(make="Nissan")
print(my_car.model)




























window.mainloop()