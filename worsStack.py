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

word = "(Test)( (Input Value)"
word2 = ")(Test New(input)"
T1 =TestStack()
for x in word:
    if x=="(":
        T1.push(x)
    elif x==")":
        if T1.pop() == None:
             print("Unbalanced Parenthesis")
if T1.pop() == None:
    print("Parenthesis is balanced")
else:
    print("Parenthesis is unbalanced")

