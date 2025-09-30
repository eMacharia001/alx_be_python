class Student :
    def __init__ (self, name, age,):
        self.name = name
        self.age = age

    def get_descriptive_name(self):
        long_name = f"{self.name}, {self.age} years old"
        return long_name.title()
    def greet_student(self):
        print(f"Hello, {self.name}!")

student = Student('Alice', 20)
print(student.get_descriptive_name())
student.greet_student()
student2 = Student('Bob', 22)
print(student2.get_descriptive_name())
student2.greet_student()
student3 = Student('Charlie', 19)
print(student3.get_descriptive_name())