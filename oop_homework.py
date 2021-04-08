class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_gr = 0

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg(self):
        all=[]
        for lst in self.grades.values():
            all.extend(lst)
        self.avg_gr = sum(all) / len(all)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
        return self.avg_gr < other.avg_gr

    def __str__(self):
        return (
        f"\nИмя: {self.name}"
        f"\nФамилия: {self.surname}"
        f"\nСредняя оценка за домашние задания: {self.avg_gr}"
        f"\nКурсы в процессе изучения: {self.courses_in_progress}"
        f"\nЗавершенные курсы: {self.finished_courses}"
        )

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.avg_gr = 0

    def avg(self):
        all=[]
        for lst in self.grades.values():
            all.extend(lst)
        self.avg_gr = sum(all) / len(all)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
        return self.avg_gr < other.avg_gr

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.avg_gr}'

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'