class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathing under water")
    def swim(self):
        print("Moving in water")


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
