class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        self.len = self.grades['Python'] + self.grades['Git']
        avg = sum(self.grades['Python'] + self.grades['Git']) / len(self.len)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.avg_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: Введение в программирование'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}



class Reviewer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 9)

print(best_student.grades)

some_lecturer = Lecturer('Some', 'Buddy')

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_in_progress += ['Python']

cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)

print(some_reviewer)

print(some_lecturer.grades)
print(best_student)

