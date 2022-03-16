class Student:
    '''
    Класс студентов.
    '''

    def __init__(self, name, surname, gender):  #инициализация класса студент.
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_finished = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_hw(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.average_rating:
                lectur.average_rating[course] += [grade]
            else:
                lectur.average_rating[course] = [grade]
        else:
            return 'Ошибка'


    def mid_grade(self): #подсчёт средней оценки для студента
        new = []
        for i in self.grades.values():
            new += i
        mid_grades = round(sum(new) / len(new), 1)
        return mid_grades

    def add_in_lis(self):
        lis_student = []
        if isinstance(self, Student):
            lis_student.append(self)
        else:
            return 'invalid class'


    def __str__(self):  #вывод данных об объекте класса студент
        text = f'Student:\nName: {self.name}\nSurname: {self.surname}\n\
Courses finished: {", ".join(self.courses_finished)}\n\
Courses in progress: {", ".join(self.courses_in_progress)}\nAverage rating: {self.mid_grade()}'  #дописать вывод средней оценки
        return text


class Mentor:
    '''
    Клас менторов. Общий (родительский) для всех типов преподавателей.
    '''

    def __init__(self, name, lastname, courses_attached):  #инициализация класса менторов
        self.name = name
        self.lastname = lastname
        self.courses_attached = []


    def __str__(self):  #вывод информации о классе менторов
        text = f'Имя: {self.name}\nФамилия: {self.lastname}'
        return text


class Lecturer(Mentor):
    '''
    Инициализация класса лекторов с наследованием класса менторов.
    '''
    def __init__(self, name, lastname, courses_attached):   #инициализация класса лекторов с наследованием класса менторов
        super().__init__(name, lastname, courses_attached)
        self.courses_attached = []
        self.average_rating = {}


    def mid_grade_(self):
        new = []
        for i in self.average_rating.values():
            new += i
        mid_grades_ = round(sum(new) / len(new), 1)
        return mid_grades_

    def add_in_lis(self):
        lis_lectur = []
        if isinstance(self, Lecturer):
            lis_lectur.append(self)
        else:
            return 'invalid class'


    def __str__(self):   #вывод информации о классе лекторов
        text = f'Lectur:\nName: {self.name}\nSurname: {self.lastname}\nAverage rating: {self.mid_grade_()}'
        return text


class Reviewer(Mentor):
    '''
     Инициализация класса проверяющих с наследованием от класса менторов.
    '''
    def __init__(self, name, lastname, courses_attached, work_evaluation=True):  #инициализация класса проверяющих с наследованием от класса менторов
        super().__init__(name, lastname, courses_attached)
        self.courses_attached = []


    def __str__(self):   #вывод информации об объекте класса проверяющих
        description = f'Reviewer:\nName: {self.name}\nSurname: {self.lastname}'
        return description


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and 0 <= grade <= 10:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def perform_comparison(student1, student2):  #функция сравнения успеваемости студентов
    if isinstance(student1, Student) and isinstance(student2, Student):
        if student1.mid_grade() > student2.mid_grade():
            return f'Student performance {student1.name} better. Average score {student1.mid_grade()}'
        else:
            return f'Student performance {student2.name} better. Average score {student2.mid_grade()}'
    else:
        return 'Error. Invalid class.'

# первый студент
stud1 = Student('Mark', 'Tven', 'man')
# второй студент
stud2 = Student('Alen', 'Delon', 'man')
# первый лектор
lectur1 = Lecturer('Che', 'Gevarra', 'Python')
# второй лектор
lectur2 = Lecturer('Poligraf', 'Sharikov', 'Python')
# первый ревьювер
review1 = Reviewer('Albert', 'Einstein', 'Python')
# второй ревьювер
review2 = Reviewer('Nikola', 'Tesla', 'Python')
stud1.courses_in_progress += ['Python', 'Jango']
stud1.courses_finished += ['Введение в программирование', 'GIT']
stud1.rate_hw(lectur1, 'Python', 9)
stud1.rate_hw(lectur1, 'Python', 10)
stud1.rate_hw(lectur1, 'Python', 9)
stud1.add_in_lis()
stud2.courses_in_progress += ['Python', 'GIT']
stud2.courses_finished += ['Введение в программирование', 'Big Data']
stud2.add_in_lis()
lectur1.courses_attached += ['Python']
review1.rate_hw(stud1, 'GIT', 9)
review1.courses_attached += ['Python']
review1.rate_hw(stud1, 'Python', 10)
review1.rate_hw(stud1, 'Python', 9)
review1.rate_hw(stud1, 'Python', 8)
review2.courses_attached += ['Python', 'GIT', 'Django']
review2.rate_hw(stud2, 'Python', 9)
review2.rate_hw(stud2, 'Python', 1)
review2.rate_hw(stud2, 'GIT', 1)

print(perform_comparison(stud1, stud2)) #сравнение успеваемости студентов
