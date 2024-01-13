class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students.append(self)

    def av_grade(self):
        all_grades = []
        for course in self.grades:
            all_grades += self.grades[course]
        av = sum(all_grades) / len(all_grades)
        return round(av, 1)

    def add_course(self, course):
        self.finished_courses.append(course)
    
    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress 
            or course in self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
    
    def __str__(self):
        finished_courses_str = (''.join(self.finished_courses) 
                                if self.finished_courses else "нет завершенных курсов")
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.av_grade()}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {finished_courses_str}"
        )
    
    def compare(self, other):
        compare_dict = {
            's1': [self, self.av_grade()],
            's2': [other, other.av_grade()]
        }

        if compare_dict['s1'][1] == compare_dict['s2'][1]:
            return f"Средние оценки студентов равны и составляют {compare_dict['s1'][1]}"
        
        best_student = max(compare_dict, key=lambda k: compare_dict[k][1])
        name = compare_dict[best_student][0].name
        surname = compare_dict[best_student][0].surname
        grade = compare_dict[best_student][1]
        return f"Средняя оценка выше у студента {name} {surname} и составляет {grade}"
    
    def __eq__(self, other):
        s1 = self.av_grade()
        s2 = other.av_grade()

        if s1 == s2:
            return f"Средние оценки студентов равны и составляют {s1} баллов"
        else:
            return "Средние оценки студентов не равны"
    
    def __gt__(self, other):
        s1 = self.av_grade()
        s2 = other.av_grade()

        if s1 > s2:
            return f"Средняя оценка студента {self.name} {self.surname} выше и составляет {s1} баллов"
        else:
            return f"Средняя оценка студента {self.name} {self.surname} не выше оценки студента {other.name} {other.surname}"
    
    def __lt__(self, other):
        s1 = self.av_grade()
        s2 = other.av_grade()

        if s1 < s2:
            return f"Средняя оценка студента {self.name} {self.surname} ниже и составляет {s1} баллов"
        else:
            return f"Средняя оценка студента {self.name} {self.surname} не ниже оценки студента {other.name} {other.surname}"


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        all_lectors.append(self)

    def av_grade(self):
        all_grades = []
        for course in self.grades:
            all_grades += self.grades[course]
        av = sum(all_grades) / len(all_grades)
        return round(av, 1)
    
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.av_grade()}"
        )
    
    def compare(self, other):
        compare_dict = {
            'l1': [self, self.av_grade()],
            'l2': [other, other.av_grade()]
        }

        if compare_dict['l1'][1] == compare_dict['l2'][1]:
            return f"Средние оценки лекторов равны и составляют {compare_dict['l1'][1]}"
        
        best_lector = max(compare_dict, key=lambda k: compare_dict[k][1])
        name = compare_dict[best_lector][0].name
        surname = compare_dict[best_lector][0].surname
        grade = compare_dict[best_lector][1]
        return f"Средняя оценка выше у лектора {name} {surname} и составляет {grade}"
    
    def __eq__(self, other):
        l1 = self.av_grade()
        l2 = other.av_grade()

        if l1 == l2:
            return f"Средние оценки лекторов равны и составляют {l1} баллов"
        else:
            return "Средние оценки лекторов не равны"
    
    def __gt__(self, other):
        l1 = self.av_grade()
        l2 = other.av_grade()

        if l1 > l2:
            return f"Средняя оценка лектора {self.name} {self.surname} выше и составляет {l1} баллов"
        else:
            return f"Средняя оценка лектора {self.name} {self.surname} не выше оценки лектора {other.name} {other.surname}"
    
    def __lt__(self, other):
        l1 = self.av_grade()
        l2 = other.av_grade()

        if l1 < l2:
            return f"Средняя оценка лектора {self.name} {self.surname} ниже и составляет {l1} баллов"
        else:
            return f"Средняя оценка лектора {self.name} {self.surname} не ниже оценки лектора {other.name} {other.surname}"


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка")
    
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )
    

all_students = []
all_lectors = []


def av_students_course_grade(course):
    all_grades = []
    for s in all_students:
        if course in s.courses_in_progress:
            all_grades += s.grades[course]

    if all_grades:
        return f"Средняя оценка студентов по курсу {course}: {sum(all_grades) / len(all_grades)}"
    else:
        return f"Нет оценок по курсу {course}"
    
def av_lectors_course_grade(course):
    all_grades = []
    for l in all_lectors:
        if course in l.courses_attached:
            all_grades += l.grades[course]
            
    if all_grades:
        return f"Средняя оценка лекторов по курсу {course}: {sum(all_grades) / len(all_grades)}"
    else:
        return f"Нет оценок по курсу {course}"
    

reviewer1 = Reviewer('Nick', 'Peterson')
reviewer1.courses_attached += ['Robotics']

reviewer2 = Reviewer('Kate', 'Alison')
reviewer2.courses_attached += ['Wall crawling']

student1 = Student('May', 'Green', 'female')
student1.courses_in_progress += ['Robotics']
student1.courses_in_progress += ['Wall crawling']
student1.add_course('Sword fighting')
reviewer1.rate_hw(student1, 'Robotics', 10)
reviewer2.rate_hw(student1, 'Wall crawling', 8)

student2 = Student('Ray', 'Brown', 'male')
student2.courses_in_progress += ['Robotics']
student2.courses_in_progress += ['Wall crawling']
reviewer1.rate_hw(student2, 'Robotics', 10)
reviewer2.rate_hw(student2, 'Wall crawling', 4)

lector1 = Lecturer('Tony', 'Stark')
lector1.courses_attached += ['Robotics']
student1.rate_l(lector1, 'Robotics', 10)
student2.rate_l(lector1, 'Robotics', 8)

lector2 = Lecturer('Peter', 'Parker')
lector2.courses_attached += ['Wall crawling']
student1.rate_l(lector2, 'Wall crawling', 10)
student2.rate_l(lector2, 'Wall crawling', 6)

print(reviewer1)
print()
print(reviewer2)
print()
print(lector1)
print()
print(lector2)
print()
print(student1)
print()
print(student2)
print()

print(student1.compare(student2))
print(student1 == student2)
print(student1 > student2)
print(student1 < student2)
print()

print(lector1.compare(lector2))
print(lector1 == lector2)
print(lector1 > lector2)
print(lector1 < lector2)
print()

print(av_students_course_grade('Robotics'))
print(av_students_course_grade('Wall crawling'))
print(av_students_course_grade('Sword fighting'))
print()

print(av_lectors_course_grade('Robotics'))
print(av_lectors_course_grade('Wall crawling'))
print(av_lectors_course_grade('Sword fighting'))