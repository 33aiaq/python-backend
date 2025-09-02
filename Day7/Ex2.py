class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create instances
person1 = Person("Ahmad", 27)
person2 = Person("Yousef", 25)

# Call introduce()
print(person1.introduce())
print(person2.introduce())
