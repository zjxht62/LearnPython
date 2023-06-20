class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_str(cls, full_name):  # 类cls作为参数传递进来，
        first_name, last_name = map(str, full_name.split(' '))
        student = cls(first_name, last_name)  # 调用构造方法
        return student


if __name__ == '__main__':
    student1 = Student("James", "May")
    student2 = Student.from_str("Jeremy Clarkson")
