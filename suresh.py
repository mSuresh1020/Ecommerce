class Rohit:
    def __init__(self,n):
        self.name=n
        print("hello",n)
    def method(self):
        print('Brain_work is great place for placement')
roo=Rohit('Madhuri')

def pickling():
    import pickle
    with open('first_data.txt','wb') as f1:
        data=pickle.dump(roo,f1)
        print(data)
res=pickling()

def unpicklig():
    import pickle
    with open('first_data.txt','rb') as f2:
        data1=pickle.load(f2)
        return data1
u=unpicklig()
u.method()

A=iter([10,20,30,60])
# for i in A:
print(next(A))
print(type(A))

# def csv_file(roo_txt):
#     for i in open('roo.txt','r'):
#         if [x for x in data if x<len(50)]:
#             yield i
#             roo.txt.read().split('.')

#
# a=int(input('Enter no:'))
# b=int(input('Enter no:'))
# c=int(input('Enter no:'))
# d=a**3+b**3+c**3
# e=100*a+10*b+1*c
# if d==e:
#     print('This is armstrong no:',e)
# else:
#     print('This is  no armstrong :',e)
#
# def factorial(num):
#     if num==0:
#         fact=1
#     else:
#         fact=num*factorial(num-1)
#     return fact
# num=factorial(5)
# print(num)