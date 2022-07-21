class student():
    def __init__(self,age,course,grade,name):
        self.age = age
        self.name = name
        self.grade = grade
        self.course = course
    def function(self):
        print("Hello my name is ", self.name, " I am ", self.age, " years old with an average grade of ", self.grade, " in ", self.course)
p1 = student(18,"BioMed",9.5, "Steven")
p1.function()
