#program to implement a stack

class TestStack:
    def __init__(self):
        self.__stackTest = []

    def push(self,data):
        self.__stackTest.append(data)

    def pop(self):
        if len(self.__stackTest) == 0:
            return None
        else:
            value = self.__stackTest.pop(-1)
            return value

T1 =TestStack()
T1.push({"id":1,"msg":"test"})
T1.push({"id":2,"msg":"test2"})
T1.push({"id":3,"msg":"test3"})
T1.push({"id":4,"msg":"test4"})
print(T1.pop())
print(T1.pop())
print(T1.pop())



