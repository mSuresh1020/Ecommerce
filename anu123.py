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
