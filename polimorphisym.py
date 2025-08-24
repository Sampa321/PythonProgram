# class Overloadinexample:
#     def sum(n):
#         print(n)
#     def sum(n1,n2):
#         print("sum=",n1+n2)
#     def sum(n1,n2,n3):
#         print("sum=",n1+n2+n3)
# a=Overloadinexample()
# a.sum(12,2,2)
class Addition:
    def sum(self,n1=None,n2=None,n3=None):
        if(n1!=None and n2!=None and n3!=None):
            print("sum=",n1+n2+n3)
        elif(n1!=None and n2!=None):
            print("sum=",n1+n2)
        else:
            print("Please enter atleast two value")
obj=Addition()
obj.sum(10,20,30)
obj.sum(10,20)
obj.sum(10)