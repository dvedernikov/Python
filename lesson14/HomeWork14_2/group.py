from student import Student

class GroupLimitExceededError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.massege = message
        super().__init__(self.massege)

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