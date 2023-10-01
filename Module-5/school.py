class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self):
        return f'Student with name: {self.name},class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Tearcher : {self.name}, subject:{self.subject}'
    

class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            print ('not enough fee')
        else:
            id = len(self.students)+1
            student = Student(name,'c',id)
            self.students.append(student)
            print (f'{name} is enrolled with id: {id}, extra money {fee-6500}')
        

    def __repr__(self):
        print('welcome to',self.name)
        print('-------our Tearchers-------')
        for teacher in self.teachers:
            print(teacher)
        print('--------Our Students--------')
        for student in self.students:
            print(student)
        return 'All done for now'

# dalia = Student('dalia',9,1)
# arkan = Teacher('Ali mia','algorithm',101)
# print(dalia)
# print(arkan)

phitron = School('phitron')
phitron.enroll('dalia',5900)
phitron.enroll('dali',5800)
phitron.enroll('alia',5700)

phitron.add_teacher('Arkanul','DS')
phitron.add_teacher('anul','algo')
phitron.add_teacher('Arka','data')
print(phitron)