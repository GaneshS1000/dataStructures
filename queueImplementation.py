#program to implement a queue data structure

class TestQueue:

    def __init__(self):
        self.__queueTest = []

    def enQueue(self,data):
        self.__queueTest.append(data)

    def deQueue(self):
        if len(self.__queueTest) == 0:
            return None
        else:
            value = self.__queueTest.pop(0)
            return value

class MsgQueue(TestQueue):
    def __init__(self):
        super().__init__()

    def enQueue(self,data):
        if list(data.keys())==["id","msg"]:
            super().enQueue(data)
        else:
            print("data validation failed",data.keys())
    '''def deQueue(self):
        return super().deQueue()'''

T1 = MsgQueue()
T1.enQueue({'id':1,"msg":"test"})
T1.enQueue({"id":2,"msg":"test2"})
print(T1.deQueue())
print(T1.deQueue())
print(T1.deQueue())

