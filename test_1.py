#coding=utf-8
from selenium import webdriver
import math
import DateTime


# a=5
# if a<0:
#     print("a")
# elif a<6:
#     print("b")
# else:
#     print("c")

def Compared():
    A=int(input("输入数字1："))
    B=int(input("输入数字2："))
    print(max(A,B))
    if A>=B:
        print(A)

    else:
        print(B)

def inputmath():
    D = int(input("输入数字："))
    print(len(D))

    C = int(input("输入数字"))
    if C<0:
        print("格式不正确")
    elif C<100000:
        if C<10:
            print(1)
        elif C<100:
            print(2)
        elif C<1000:
            print(3)
        elif C<10000:
            print(4)
        else :
            print(5)
    else:
        print("输入一个小于5位数的数字")

def cut():
    list = ['A','B','C','D','E','F','G','H']
    print(list[:4])
    print(list[2:4])
    print(list[1:])
    print(list[0:5])
    print(list[-4:])
    print(list[1])


# for i in range(10):
#     if i&1:
#         continue
#     print(i)
#
# for i in range(0,10,2):
#     print(i)

# list=["A","B","c"]
# list.reverse()
# print(list)


def input_math_1():
    #给定一个数字，判断该数的位数，依次打印出个位，十位，百位，千位，万位的数字
    A=int(input("输入"))
    if 0<=A<10:
        print(1)
    elif 0<A<100:
        print(2)
    elif 0<A<1000:
        print(3)
    elif 0<A<10000:
        print(4)
    elif 0<A<100000:
        print(5)
    else:
        print("输入有效数字")
    B = list(str(A))
    B.reverse()
    for x in B:
        print(x)
#input_math_1()

def input_math_2():
    '''假设输入数字是54321
    第一趟：54321//10=5432
        54321-5432*10=1
    第二趟：5432//10=543
        5432-543*10=2
    '''
    val = int(input("输入"))
    if val>=1000:       #折半思想
        if val>=10000:
            num=5
        else:
            num=4
    else:
        if val>=100:
            num=3
        elif val>=10:
            num=2
        else:
            num=1
    print(num)
    c=val
    for i in range(num):
        n=c//10
        print(c-n*10)
        c=n

def input_math_3():
    #给定一个数字，判断该数的位数，依次打印出个位，十位，百位，千位，万位的数字
    A=int(input("输入"))
    if 0<=A<10:
        print(1)
    elif 0<A<100:
        print(2)
    elif 0<A<1000:
        print(3)
    elif 0<A<10000:
        print(4)
    elif 0<A<100000:
        print(5)
    else:
        print("输入有效数字")
    B=str(A)
    C=len(B)
    for i in range(C):
        print(A % 10)
        A = A // 10

#input_math_3()

#1.打印边长位n的正方形
def square():
    n=int(input("正方形边长"))
    # print("*"*n)
    # for x in range(n-2):
    #     print("*",""*(n-2),"*")
    # print("*"*n)
    setTop="*"
    setMid="*"
    for i in range(0,n):
        setTop +="\t*"
        setMid +="\t"
    else:
        setMid +="*"
        print(setTop)

    for i in range(0,n-1):
        print("\n")
        print(setMid)
    else:
        print("\n")
        print(setTop)



#2.求100内所有奇数的和
# list_M=[]
# sum=0
# for x in range(100):
#     if x%2!=0:
#         list_M.append(x)
# for i in list_M:
#     sum=i+sum
# print(sum)

# sum = 0
# for i in range(1,100,2):
#     sum+=i
# print(sum)

#3.判断学生的成绩，成绩等级A-E，其中，90分以上为"A"，80-89为B，70-79为C，60-69为D，60分以下为E
def score():
    core=int(input("学生成绩"))
    if 0<=core<=100:
        if core>=80:
            if core>=90:
                print("学生成绩为A")
            else:
                print("学生成绩为B")
        else:
            if core>=70:
                print("学生成绩为C")
            elif core>=60:
                print("学生成绩为D")
            else:
                print("学生成绩为E")
    else:
        print("输入有效成绩")

#求1到5阶乘之和
def factorial():
    sum=0
    num=1
    for x in range(1,6):
        A=x*num
        sum+=A
        num=A
    print(sum)
# sum1=0
# num=1
# F=[]
# for x in range(1,6):
#     A = x * num
#     num=A
#     F.append(A)
# print(sum(F))


#给一个数，判断它是否是素数（质数）  质数：一个大于1的自然数只能被1和它本身整除
def Prime_number():
    num=int(input("数字"))
    if num>1:
        for x in range(2,num):
            if num%x==0:
                print("不是质数")
                break
        else:
            print("是质数")
    else:
        print("输入自然数")



# prime_number=[]
# for x in range(2,100):
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         prime_number.append(x)
# #print(len(prime_number))
# print(prime_number)

# prime_number1=[2]
# for x in range(3,100):
#     for i in prime_number1:
#         if x%i==0:
#             break
#     else:
#         prime_number1.append(x)
# #print(len(prime_number))
# print(prime_number1)
# primenumber=[]
# flag = False
# for x in range(2,100000):
#     for i in primenumber:
#         if x%i==0:
#             flag = False
#             break
#         if i>=math.ceil(math.sqrt(x)):
#             flag = False
#             break
#     if not flag:
#         print(x)
#         primenumber.append(x)


#print(type(math.sqrt(100)))

# for x in range(1,10):
#     for i in range(1,x):
#         print(x,i)

#杨辉三角  方法1
# triangle = [[1],[1,1]]
# n = 7
# for x in range(2,n):
#     pre = triangle[x-1]
#     cur = [1]
#     for i in range(0,x-1):
#         cur.append(pre[i]+pre[i+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)

#方法2
# triangle = []
# n = 7
# triangle.append([1])
# for x in range(1,n):
#     pre = triangle[x-1]
#     cur = [1]
#     if x!=1:
#         for i in range(0,x-1):
#             cur.append(pre[i]+pre[i+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)


#方法3
# n=6
# oldline = []
# newline = [1]
# length = 0
# print(newline)
# for i in range(1,n):
#     oldline = newline.copy()
#     oldline.append(0)  #尾部加0，相当于2端加0
#     print(oldline)
#     newline.clear()
#     offset = 0
#     for j in range(i+1):
#         newline.append(oldline[offset-1] + oldline[offset])
#         offset+=1
#     #print(newline)

n=100
pn = []
flag = False
count = 0
start = DateTime.DateTime

for x in range(2,n):
    for i in pn:
        count += 1
        if x%i==0:
            flag = True
            break
        if i >= math.ceil(x**0.5):
            flag = False
            break
    if not flag:
        pn.append(x)
print(pn)
delta = (DateTime.DateTime.now() - start).total_seconds
print(count)
