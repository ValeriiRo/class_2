class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def evaluation_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_ratings = 0
        number_ratings = 0
        for list_ratings in lecturer.grades.values():
            for rating in list_ratings:
                sum_ratings += rating
                number_ratings += 1
        lecturer.average_rating = sum_ratings / number_ratings

    def __str__(self):
        object = f"Студент: \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
                 f"{self.average_rating}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return object

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является Лектором!')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = 0
        self.grades = {}

    def __str__(self):
        object = f'Лектор: \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return object

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_ratings = 0
        number_ratings = 0
        for list_ratings in student.grades.values():
            for rating in list_ratings:
                sum_ratings += rating
                number_ratings += 1
        student.average_rating = sum_ratings / number_ratings

    def __str__(self):
        object = f'Проверяющий: \nИмя: {self.name}\nФамилия: {self.surname}'
        return object

def new_student(list_student):
    student_name = Student(input('Имя студента: '), input('Фамилия студента: '), input('Пол студента: '))
    if student_name.name == 'end' or student_name.surname == 'end' or student_name.gender == 'end':
        return
    for student in list_student:
        if student_name.name == student.name and student_name.surname == student.surname and student_name.gender == student.gender:
            print('Данный экземпляр уже существует!')
            to_create = input('Создать? (y - да, n - нет): ')
            if to_create == 'n':
                return
    list_student += [student_name]
    return list_student

def finished_courses_student(list_student, student):
    operations = input('Добавить(add) или удалит(del) завершённый курс?')
    if operations == 'add':
        finished_courses = input('Введите название завершенного курса: ')
        student.finished_courses += [finished_courses]
    elif operations == 'del':
        finished_courses = input('Введите название завершенного курса(который требуется удалить): ')
        if finished_courses in student.finished_courses:
            student.finished_courses.remove(finished_courses)
        else:
            print('Курса нет в списке!')
    elif operations == 'end':
        return
    else:
        print('Введена не существующая команда! Добавить - add, удалит - del, завершить выполнение - end ')
        finished_courses_student(list_student, student)
    return (list_student)

def courses_in_progress_student(list_student, student):
    operations = input('Добавить(add) или удалит(del) курс?')
    if operations == 'add':
        courses_in_progress = input('Введите название курса: ')
        student.courses_in_progress += [courses_in_progress]
    elif operations == 'del':
        courses_in_progress = input('Введите название курса(который требуется удалить): ')
        if courses_in_progress in student.courses_in_progress:
            student.courses_in_progress.remove(courses_in_progress)
        else:
            print('Курса нет в списке!')
    elif operations == 'end':
        return
    else:
        print('Введена не существующая команда! Добавить - add, удалит - del, завершить выполнение - end ')
        courses_in_progress_student(list_student, student)
    return (list_student)

def working_students(list_student):
    executing_сommand = 'student'
    print('Работа со студентами')
    imp_command = input('Введите команду: ').lower()

    if 'help' == imp_command:
        help(executing_сommand)

    elif 'add' == imp_command:
        new_student(list_student)

    elif 'info' == imp_command or 'fc' == imp_command or 'finished_courses' == imp_command or 'cp' == imp_command or 'courses_in_progress' == imp_command:
        name_student, surname_student = input('Введите имя студента: '), input('Введите фамилию студента: ')
        for student in list_student:
            if name_student == student.name:
                if surname_student == student.surname:

                    if 'info' == imp_command:
                        print(student)
                        working_students(list_student)

                    elif 'fc' == imp_command or 'finished_courses' == imp_command:
                        finished_courses_student(list_student, student)
                        working_students(list_student)

                    elif 'cp' == imp_command or 'courses_in_progress' == imp_command:
                        courses_in_progress_student(list_student, student)
                        working_students(list_student)

        print('Студента нет в списке!')

    elif 'all_info' == imp_command:
        for student in list_student:
            print(f'{student}\n')

    elif 'end' == imp_command:
        executing_сommand = 'non'

    else:
        print("Введена не существующая команда! Воспользуйтесь 'help' для получения перечьня команд!")

    if executing_сommand == 'student':
        working_students(list_student)

    else:
        return list_student

def new_lecturer(list_lecturer):
    lecturer_name = Lecturer(input('Имя лктора: '), input('Фамилия лектора: '))
    if lecturer_name.name == 'end' or lecturer_name.surname == 'end':
        return
    for lekturer in list_lecturer:
        if lecturer_name.name == lekturer.name and lecturer_name.surname == lekturer.surname:
            print('Данный экземпляр уже существует!')
            to_create = input('Создать? (y - да, n - нет): ')
            if to_create == 'n':
                return
    list_lecturer += [lecturer_name]
    return list_lecturer

def courses_attached_lecturer(list_lecturer, lecturer):
    operations = input('Добавить(add) или удалит(del) курс?')
    if operations == 'add':
        courses_attached = input('Введите название курса: ')
        lecturer.courses_attached += [courses_attached]
    elif operations == 'del':
        courses_attached = input('Введите название курса(который требуется удалить): ')
        if courses_attached in lecturer.courses_attached:
            lecturer.courses_attached.remove(courses_attached)
        else:
            print('Курса нет в списке!')
    elif operations == 'end':
        return
    else:
        print('Введена не существующая команда! Добавить - add, удалит - del, завершить выполнение - end ')
        courses_attached_lecturer(list_lecturer, lecturer)
    return (list_lecturer)

def working_lecturers(list_lecturer):
    executing_сommand = 'lecturer'
    print('Работа с лекторами')
    imp_command = input('Введите команду: ').lower()

    if 'help' == imp_command:
        help(executing_сommand)

    elif 'add' == imp_command:
        new_lecturer(list_lecturer)

    elif 'info' == imp_command or 'ca' == imp_command or 'courses_attached' == imp_command:
        name_lecturer, surname_lecturer = input('Введите имя лектора: '), input('Введите фамилию лектора: ')
        for lecturer in list_lecturer:
            if name_lecturer == student.name:
                if surname_lecturer == student.surname:

                    if 'info' == imp_command:
                        print(lecturer)
                        working_students(list_lecturer)

                    elif 'ca' == imp_command or 'courses_attached' == imp_command:
                        courses_attached_lecturer(list_lecturer, lecturer)
                        working_lecturers(list_lecturer)

        print('Лектора нет в списке!')

    elif 'all_info' == imp_command:
        for lecturer in list_lecturer:
            print(f'{lecturer}\n')

    elif 'end' == imp_command:
        executing_сommand = 'non'

    else:
        print("Введена не существующая команда! Воспользуйтесь 'help' для получения перечьня команд!")

    if executing_сommand == 'lecturer':
        working_lecturers(list_lecturer)

    else:
        return list_lecturer

def new_reviewer(list_reviewer):
    reviewer_name = Reviewer(input('Имя эксперта: '), input('Фамилия эксперта: '))
    if reviewer_name.name == 'end' or reviewer_name.surname == 'end':
        return
    for reviewer in list_reviewer:
        if reviewer_name.name == reviewer.name and reviewer_name.surname == reviewer.surname:
            print('Данный экземпляр уже существует!')
            to_create = input('Создать? (y - да, n - нет): ')
            if to_create == 'n':
                return
    list_reviewer += [reviewer_name]
    return list_reviewer

def courses_attached_reviewer(list_reviewer,reviewer):
    correct_assessment = False
    correct_course  = False
    name_student, surname_student = input('Введите имя студента: '), input('Введите фамилию студента: ')
    for student in list_student:
        if name_student == student.name:
            if surname_student == student.surname:
                print('Оценка за домашнее задание')
                while correct_course == False:
                    course = input('Введите название курса: ')
                    if course in student.courses_in_progress:
                        correct_course = True
                    else:
                        print('Неверный курс!')
                while correct_assessment == False:
                    estimation = input('Введите оценку по деситибальной шкале(от 1 до 10): ')
                    if estimation == '1' or estimation == '2' or estimation == '3' or estimation == '4' or estimation == '5' or estimation == '6' or estimation == '7' or estimation == '8' or estimation == '9' or estimation == '10':
                        estimation = int(estimation)
                        correct_assessment = True
                    else:
                        print('Некорректная оценка!')
                reviewer.rate_hw(student, course, estimation)
                return (list_reviewer,reviewer)
    print('Студента нет в списке!')
    courses_attached_reviewer(list_reviewer, reviewer)

def working_reviewer(list_reviewer):
    executing_сommand = 'reviewer'
    print('Работа с экспертами')
    imp_command = input('Введите команду: ').lower()

    if 'help' == imp_command:
        help(executing_сommand)

    elif 'add' == imp_command:
        new_reviewer(list_reviewer)

    elif 'info' == imp_command or 'courses_attached' == imp_command or 'ca' == imp_command:
        name_reviewer, surname_reviewer = input('Введите имя эксперта: '), input('Введите фамилию эксперта: ')
        for reviewer in list_reviewer:
            if name_reviewer == reviewer.name:
                if surname_reviewer == reviewer.surname:

                    if 'info' == imp_command:
                        print(reviewer)
                        working_reviewer(list_reviewer)

                    elif 'courses_attached' == imp_command or 'ca' == imp_command:
                        courses_attached_reviewer(list_reviewer, reviewer)
                        working_reviewer(list_reviewer)

        print('Эксперта нет в списке!')

    elif 'all_info' == imp_command:
        for reviewer in list_reviewer:
            print(f'{reviewer}\n')

    elif 'end' == imp_command:
        executing_сommand = 'non'

    else:
        print("Введена не существующая команда! Воспользуйтесь 'help' для получения перечьня команд!")

    if executing_сommand == 'reviewer':
        working_reviewer(list_reviewer)

    else:
        return list_reviewer

def help(executing_сommand):
    print('перечень команд:')
    print('Команды с табуляцией можно использовать в рамках конкретного класса')
    print('student - команда для работы со студентами')
    print('\tadd - команда для добавления нового экземпляра')
    print('\tfc (finished_courses) - команда для добавление и удаление завершённых курсов студента')
    print('\tcp (courses_in_progress) - команда для добавление и удаление курсов а процессе студента')
    print('\tinfo - информация по конкретному студенту')
    print('\tall_info - информация по всем студентам')
    print('\tend - завершить работу со студентами')
    print('lecturer - команда для работы с лекторами')
    print('\tadd - команда для добавления нового экземпляра')
    print('\tca (courses_attached) - добавить или удалить курс на которм преподаёт лектор')
    print('\tend - завершить работу со лекторами')
    print('Reviewer - команда для работы с экспертами')
    print('\tadd - команда для добавления нового экземпляра')
    print('\tca (courses_attached) - выставление оценки за домашнюю работу')
    print('\tend - завершить работу со лекторами')
    print('all_info - информация по всем студентам, лекторам и экмпертам')
    print('end - Выход из программы')
    return(executing_сommand)

executing_сommand = 'non'
end = False
list_student = []
list_lecturer = []
list_reviewer = []

lecturer = Lecturer('Tailer', 'Durden')
lecturer.courses_attached += ['Git']
list_lecturer += [lecturer]

lecturer = Lecturer('r', 'r')
lecturer.courses_attached += ['r']
list_lecturer += [lecturer]

reviewer = Reviewer('r', 'r')
reviewer.courses_attached += ['r']
list_reviewer += [reviewer]

reviewer = Reviewer('Peter', 'Pedigree')
reviewer.courses_attached += ['python']
list_reviewer += [reviewer]

student = Student('r', 'r', 'r')
student.courses_in_progress += ['r', 'Git']
student.finished_courses += ['Введение в программирование']
list_student += [student]

student = Student('Robert', 'Paulsen', 'your_gender')
student.courses_in_progress += ['python', 'Git']
student.finished_courses += ['Введение в программирование']
list_student += [student]

while end == False:
    print('Главное меню')
    imp_command = input('Введите команду: ').lower()

    if 'student' == imp_command:
        working_students(list_student)

    elif 'lecturer' == imp_command:
        working_lecturers(list_lecturer)

    elif 'reviewer' == imp_command:
        working_reviewer(list_reviewer)

    elif 'all_info' == imp_command:
        for student in list_student:
            print(f'{student}\n')

    elif 'end' == imp_command:
        end = True

    elif 'help' == imp_command:
        help(executing_сommand)
        if 'student' == executing_сommand:
            working_students(list_student)
        elif 'lecturer' == executing_сommand:
            working_lecturers(list_lecturer)
        elif 'reviewer' == executing_сommand:
            working_reviewer(list_reviewer)

    else:
        print("Введена не существующая команда! Воспользуйтесь 'help' для получения перечьня команд!")

