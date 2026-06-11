1
class Car:
    brand= "Toyota"
    model="Yaris"

car_type=Car()
print(car_type.brand, car_type.model)

2
class Rectangle:
    length = 5
    width = 10

    def area(self):              # method INSIDE class
        return self.length * self.width

rect = Rectangle()
print(f"Area of rectangle: {rect.length} * {rect.width} = {rect.area()}")
# Area of rectangle: 5 * 10 = 50


class Student:
    name = "Babalola"
    score = 75

    def is_passed(self):          # method INSIDE class
        return self.score >= 50   # returns True or False

student_info = Student()
print(student_info.is_passed())   # True (75 < 50)