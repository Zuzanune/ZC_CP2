#ZC 2nd class notes
import random
#EX 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.title = breed.capitalize()
        self.age = age
    def __str__(self):
        return f"Name: {self.name}\nTitle: {self.title}\nAge: {self.age}"
    def speak(self):
        return f"{self.name} says woof!"

"""doug = Dog("doug", "golden retriever", 3)
pongo = Dog("pongo", "dalmatian", 8)
if 1 < 9:
    print(doug)
    print(pongo)
    objects = [doug, pongo, doug]
    print(random.choice(objects).speak())"""
#EX 2:
class ClassSubject:
    def __init__(self, name, teacher = "Ms.LaRose", room = None):
        self.name = name.capitalize()
        self.teacher = teacher.capitalize()
        self.room = room.capitalize()
    def __str__(self):
        return f"Name: {self.name}\nTeacher: {self.teacher}\nRoom: {self.room}"
first_subject = ClassSubject("geography", "Mr. Macinanti", "213")
second_subject = ClassSubject("CSP2", "Ms. LaRose", "200")
third_subject = ClassSubject("Biology", "Ms. Krueger", "205")
fourth_subject = ClassSubject("English", "Ms. Thornock", "210")
print(first_subject)
print(second_subject)
print(third_subject)
print(fourth_subject)
