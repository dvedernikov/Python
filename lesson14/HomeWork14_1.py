class GroupLimitExceededError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):

        if len(self.group) >= 10:
            raise GroupLimitExceededError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"



try:

    gr = Group('PD1')

    for i in range(10):
        student = Student('Male', 20 + i, f"Student{i}", f"Lastname{i}", f"AN{i}")
        gr.add_student(student)

    print(gr)

    st11 = Student('Female', 25, 'Extra', 'Student', 'AN11')
    gr.add_student(st11)

except GroupLimitExceededError as e:
    print(f"Помилка: {e}")

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr_test = Group('PD2')
gr_test.add_student(st1)
gr_test.add_student(st2)
assert str(gr_test.find_student('Jobs')) == str(st1), 'Test1'
assert gr_test.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr_test.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
gr_test.delete_student('Taylor')
print(gr_test)  #
gr_test.delete_student('Taylor')
print("All tests passed!")