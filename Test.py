#coding=utf-8



#位置参数
def txt(a,b):
    print(a)
    print(b)


#默认参数
def test1(name,content='晚上好'):
    print (name,content)

#动态参数
def D_test(*args):
    print(args)

#def 形参+动态参数
def D_test1(D,*args):
    print(D)
    print(args)

#动态参数+默认参数
def zu_test(*args,moren='早上好'):
    name=""
    for item in args:
        name+=item
        name+=","

    print(args,moren)

def sum():
    count=0
    for item in range(0,100):
        count+=item
    return count


sum1=sum()

print(sum1)
txt("I am ","williams")
test1("williams")
D_test(23,4,5,7,8)
zu_test("D","W","F","H")

class Baidu():
    def shouye(self,A):
        print (A)


Baidu.shouye(Baidu(),'百度知道')