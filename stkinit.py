class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

s1 = Stack()
s1.push(1)
s1.push(2)
s1.pop()
print(s1.pop())