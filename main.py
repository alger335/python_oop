from oop_homework import *

mentor1 = Mentor('John', 'Doe')
mentor2 = Mentor('Gunter', 'Odim')

some_reviewer = Reviewer('Gannibal', 'Lecter')
some_reviewer.courses_attached += ['Hen Llinge']
some_reviewer.courses_attached += ['Magic']

some_student1 = Student('Iennefer', 'of Vengerberg', 'female')
some_student2 = Student('Sabrina', 'Glevessick', 'female')
some_student1.courses_in_progress += ['Hen Llinge']
some_student1.courses_in_progress += ['Magic']
some_student2.courses_in_progress += ['Hen Llinge']
some_student2.courses_in_progress += ['Magic']

some_lecturer1 = Lecturer('Tissaia', 'de Vries')
some_lecturer2 = Lecturer('Margarita', 'Loantile')
some_lecturer1.courses_attached += ['Hen Llinge']
some_lecturer1.courses_attached += ['Magic']
some_lecturer2.courses_attached += ['Hen Llinge']
some_lecturer2.courses_attached += ['Magic']

some_student1.rate_lc(some_lecturer1, 'Hen Llinge', 7)
some_student1.rate_lc(some_lecturer1, 'Hen Llinge', 8)
some_student1.rate_lc(some_lecturer1, 'Hen Llinge', 10)

some_student1.rate_lc(some_lecturer1, 'Magic', 9)
some_student1.rate_lc(some_lecturer1, 'Magic', 10)
some_student1.rate_lc(some_lecturer1, 'Magic', 9)

some_student1.rate_lc(some_lecturer2, 'Hen Llinge', 7)
some_student1.rate_lc(some_lecturer2, 'Hen Llinge', 8)
some_student1.rate_lc(some_lecturer2, 'Hen Llinge', 10)

some_student1.rate_lc(some_lecturer2, 'Magic', 9)
some_student1.rate_lc(some_lecturer2, 'Magic', 10)
some_student1.rate_lc(some_lecturer2, 'Magic', 9)

some_student2.rate_lc(some_lecturer1, 'Hen Llinge', 6)
some_student2.rate_lc(some_lecturer1, 'Hen Llinge', 7)
some_student2.rate_lc(some_lecturer1, 'Hen Llinge', 9)

some_student2.rate_lc(some_lecturer1, 'Magic', 6)
some_student2.rate_lc(some_lecturer1, 'Magic', 7)
some_student2.rate_lc(some_lecturer1, 'Magic', 9)

some_student2.rate_lc(some_lecturer2, 'Hen Llinge', 10)
some_student2.rate_lc(some_lecturer2, 'Hen Llinge', 10)
some_student2.rate_lc(some_lecturer2, 'Hen Llinge', 9)

some_student2.rate_lc(some_lecturer2, 'Magic', 10)
some_student2.rate_lc(some_lecturer2, 'Magic', 10)
some_student2.rate_lc(some_lecturer2, 'Magic', 9)

some_reviewer.rate_hw(some_student1, 'Hen Llinge', 5)
some_reviewer.rate_hw(some_student1, 'Hen Llinge', 6)
some_reviewer.rate_hw(some_student1, 'Hen Llinge', 6)

some_reviewer.rate_hw(some_student1, 'Magic', 7)
some_reviewer.rate_hw(some_student1, 'Magic', 8)
some_reviewer.rate_hw(some_student1, 'Magic', 9)

some_reviewer.rate_hw(some_student2, 'Hen Llinge', 6)
some_reviewer.rate_hw(some_student2, 'Hen Llinge', 10)
some_reviewer.rate_hw(some_student2, 'Hen Llinge', 10)

some_reviewer.rate_hw(some_student2, 'Magic', 9)
some_reviewer.rate_hw(some_student2, 'Magic', 8)
some_reviewer.rate_hw(some_student2, 'Magic', 9)

some_student1.avg()
some_student2.avg()
some_lecturer1.avg()
some_lecturer2.avg()

# print(mentor1)
# print(mentor2)
# print(some_reviewer)
 
# print(some_student1)
# print(some_student1.grades)
# print(some_student2)
# print(some_student2.grades)

# print(some_lecturer1)
# print(some_lecturer2)

# print(some_student1 < some_student2)
# print(some_lecturer1 < some_lecturer2)

students_list = [some_student1, some_student2]
course = 'Hen Llinge'

lecturers_list = [some_lecturer1, some_lecturer2]

def lecturers_avg(lecturers_list, course):
    grades_list = []
    all = []
    for lecturer in lecturers_list:
        grades_list.append(lecturer.grades[course])
    for lst in grades_list:
        all.extend(lst)
    return sum(all) / len(all)

print(lecturers_avg(lecturers_list, course))

def students_avg(students_list, course):
    grades_list = []
    all = []
    for student in students_list:
        grades_list.append(student.grades[course])
    for lst in grades_list:
        all.extend(lst)
    return sum(all) / len(all)

print(students_avg(students_list, course))

# grades = {'Hen Llinge': [8, 10, 9], 'C++': [10, 9, 7]}


# def avg(grades):
#     all=[]
#     for lst in grades.values():
#         all.extend(lst)
#     print(all)
#     print(sum(all) / len(all))

# avg(grades)


### Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса (в качестве аргументов принимаем список лекторов и название курса).



# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['C++']
 
# cool_lecturer = Lecturer('Gannibal', 'Lecter')
# cool_lecturer.courses_attached += ['C++']
 
# best_student.rate_lc(cool_lecturer, 'C++', 10)
# best_student.rate_lc(cool_lecturer, 'C++', 10)
# best_student.rate_lc(cool_lecturer, 'C++', 10)
 
# print(cool_lecturer.grades)


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['C++']
 
# cool_reviewer = Reviewer('First', 'Reviwer')
# cool_reviewer.courses_attached += ['C++']
 
# cool_reviewer.rate_hw(best_student, 'C++', 9)
# cool_reviewer.rate_hw(best_student, 'C++', 10)
# cool_reviewer.rate_hw(best_student, 'C++', 8)
 
# print(best_student.grades)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)
