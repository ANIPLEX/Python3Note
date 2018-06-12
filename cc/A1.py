from A2 import Peopel
class Student(Peopel):

    def __init__(self,school,name,age):
        self.school = school
        # Peopel.__init__(self,name,age)
        super(Student,self).__init__(name,age)

student1 = Student('学校','一二三',19)
print(student1.name)
print(student1.school)




