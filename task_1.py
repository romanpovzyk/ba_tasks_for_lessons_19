class Dog:

    def init(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        human_age = self.dog_age * 7
        return human_age


math = Dog(5)
print(math.human_age())