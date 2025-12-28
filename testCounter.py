#program to make use of couter Function
from collections import Counter
fruits = ["apple","banana","apple","orange","apple","orange"]
result = Counter(fruits)
print(result)
fruits.append("Kiwi")
print(result)