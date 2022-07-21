from math import sqrt
from math import pow
import random

result1 = pow(2,4)
print("result1 is ", result1)

result2 = sqrt(16)
print("resilt2 is ", result2)

result3 = random.randint(0,100)
print("result3 is ", result3)

names = ["n1","n2","n3","n4"]
print("original names ",names)

random.shuffle(names)
print("names after shuffling ", names)

result4 = random.choice(names)
print("chosen name is ", result4)