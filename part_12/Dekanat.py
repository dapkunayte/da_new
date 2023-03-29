class Student:

    def __init__(self, name:str, group, scores={}):
        self.name = name
        self.scores = {}
        if isinstance(group, Group):
            self.group = group
        else:
            print("Студента можно добавить только в группу")
        for subject, score in scores.items():
            if not(isinstance(subject, Subject) and isinstance(score, int)):
                print(f"Ошибка проставления оценки '{subject}:{score}' - значение не является оценкой")
            elif subject in self.scores.keys():
                print(f"Оценка по предмету '{subject.subject_name}' уже выставлена")
            else:
                self.scores[subject] = score

    def add_score(self, scores={}):
        for subject, score in scores.items():
            if not(isinstance(subject, Subject) and isinstance(score, int)):
                print(f"Ошибка проставления оценки '{subject}:{score}' - значение не является оценкой")
            elif subject in self.scores.keys():
                print(f"Оценка по предмету '{subject.subject_name}' уже выставлена")
            else:
                self.scores[subject] = score

    def get_average_score(self):
        if self.scores:
            scores_values = self.scores.values()
            result = sum(scores_values) / len(scores_values)
            print(f"Средняя оценка студента {self.name} равна {round(result,2)}")
        else:
            print("У студента нет оценок")


class Group:

    def __init__(self, group_name:str):
        self.group_name = group_name
        self.students = []

    def add_students(self, *args):
        for student in args:
            if not(isinstance(student, Student)):
                print(f"{student} - не является студентом")
            elif student.group.group_name != self.group_name:
                print("Группа студента отличается от той, в которую его добавляют")
            elif student in self.students:
                print(f"студент {student.name} уже в группе")
            else:
                self.students.append(student)

    def get_average_group_score(self):
        groups_score = 0
        students_with_score = 0
        if self.students:
            for student in self.students:
                if student.scores.values():
                    groups_score += sum(student.scores.values()) / len(student.scores.values())
                    students_with_score+=1
            if students_with_score != 0:
                result = groups_score/students_with_score
                print(f"Средний балл группы {self.group_name} по всем предметам равен {result}")
            else:
                print("У всех студентов нет оценок")
        else:
            print("В группе нет студентов")


class Subject:

    def __init__(self, subject_name:str, groups=[]):
        self.subject_name = subject_name
        self.groups = groups

    def get_average_subject_score_in_group(self, group):
        students_with_score = 0
        final_score = 0
        if not(isinstance(group, Group)):
            print(f"{group} - не группа")
        elif not(group in self.groups):
            print(f"Группа '{group.group_name}' не проходит предмет '{self.subject_name}'")
        else:
            for student in group.students:
                if not(self in student.scores.keys()):
                    print(f"У студента {student.name} нет оценок по предмету {self.subject_name}")
                else:
                    final_score += student.scores[self]
                    students_with_score += 1
            if students_with_score != 0:
                result = final_score/students_with_score
                print(f"Средний балл группы {group.group_name} по предмету {self.subject_name} равен {result}")
            else:
                print(f"У всех студентов в группе нет оценок по предмету {self.subject_name}")


group1 = Group("748")

subject1 = Subject("Математика", [group1])
subject2 = Subject("Русский язык", [group1])

student1 = Student("Дима", group1, {subject1: 5, subject2: 4})
student1.get_average_score()

student2 = Student("Вова", group1, {subject1: 3, subject2: 4})
student2.get_average_score()

group1.add_students(student1, student2)
group1.get_average_group_score()

subject1.get_average_subject_score_in_group(group1)

