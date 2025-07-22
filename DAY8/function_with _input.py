# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Ok then bye")
# greet()

#function that allows input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Aman")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet_with("Aman", "Delhi")
# greet_with("Delhi", "Aman") --> This will assign parameters the value in order they are passed to the function

#To stop the encounter of this error we use below syntax before passing arguments
greet_with(name="Aman", location="Delhi") #--> Here order does not matter

