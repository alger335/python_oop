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
