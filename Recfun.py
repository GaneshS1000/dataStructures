#program to make use of recursion

def fact(n):
    #fact=1
    if n>1:
        return n * fact(n -1)
    else:
        return 1

print(fact(4))

def sumupto(n):
    if n > 1:
        return n+sumupto(n-1)
    else:
        return 1
print(sumupto(3))

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1
print(fib(4))

l = [5, 4, [3, [2, 1, [4], 5], 5], [3, 2], 1]
#l is 5 4 3 2 1 4 5
def reclist(numbers):
    for i in range(len(numbers)):
        if type(i)==int:
            return numbers[i]
        else:
            return reclist(numbers[i])

print(reclist(l))