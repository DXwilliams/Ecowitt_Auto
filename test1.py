#coding=utf-8


class Test():
    classname='高中'
    def __init__(self,name,age,score,*args):
        self.name=name
        self.age=age
        self.score=score
    def mate(self,score):
        print ("数学成绩："+score)




    #类函数
    @classmethod
    def rank(cls):
        print("类方法")



    #静态函数
    @staticmethod
    def plan():
        print('静态函数')



    #实例函数
    # def userName(self,Name1):
    #     print ("他的名字是：{0}".format(Name1))

    def phy(self):

        print(self.name+"的年龄:"+self.age+",他物理考了"+self.score)

    def Admission(self,university):
        print("他被"+university+"录取了")

    #函数内调用其他函数
    def Better(self,Name1,university,*args):
        #self.userName(Name1)
        self.Admission(university)
        #return (self.name+"精通{0}学科".format(args))
        return ( self.name+"精通{0}学科".format(args))




Test.phy(Test("D","26","100"))
Test("W","25","100").phy()
Test.rank()
Test.plan()
#Test.userName("C")
print(Test.Better(Test("Z","18","100"),"MIT","English","math"))
