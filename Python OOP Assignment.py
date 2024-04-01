class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {Joseph}. I am {30} years old and I am {Male}.")

# Creating an instance of the Person class
person1 = Person("Joseph", 30, "male")
# Calling the introduce method to display the person's information
person1.introduce()
