from math import *
import random


# print(floor(3.4))   #3
# print(floor(3.6))   #3
# print(ceil(3.2))    #4
# print(ceil(3.6))    #4
# print(round(2.4))   #2
# print(round(2.5))   #2
# print(round(2.6))   #3
# print(round(3.4))   #3
# print(round(3.5))   #4
# print(round(3.6))   #4


A = [1,2,3,4,5,5,6,7]
# print(A[-1])
# print(A.index(5,-6))
# for x in A[-5:]:
#     print(x)
#
#
# A=A*5
# print(A)
B=["a","b","c"]
A.extend(B)
A.sort(key=str,reverse=True)
#print(A)


#列表复制
lst0 = list(range(4))
lst1 = list(range(4))
lst2=lst1              #内存指针指向相同位置，操作lst1，会改变lst2
lst3=lst1.copy()     #lst3赋予新的内存，lst3是一个新的列表，操作lst1无法影响lst3
# print(hash(id(lst1)))
# print(hash(id(lst2)))
# print(hash(id(lst3)))
lst5 = [1,[2,3,4],5]
lst6 = lst5.copy()
lst5[1][1] = 10       #复制的时候，中间的列表是复杂类型，所以是影子拷贝，复制内存位置
print(lst5,lst6)       #lst5修改其中的列表，修改的是内存位置的列表，导致lst6中的列表内存内容改变




R = random.randint(1,100)
T = random.choice([1,2,4,5,6])
print(R)