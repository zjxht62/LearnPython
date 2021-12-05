class A():
    def __init__(self, value):
        self.value = value

    def fun(self):
        print(self.value)


class B(A):
    def __init__(self, value):
        super().__init__(value)

    def fun(self):
        super().fun()
        # super(B, self).fun()
        print("BBB")

if __name__ == '__main__':
    b1 = B("B1")
    b1.fun()


    b2 = super(A).__init__("B1")
    print(type(b2))


