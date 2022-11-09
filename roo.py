data="""
A context manager usually takes care of setting up some resource,
e.g. opening a connection. and automatically handles the clean up when we are done with it.
Probably, the most common use case is opening a file.
Is open a context manager in Python?
You are not using the open function as a context manager.
It is the result of the open(...) call expression that is the context manager.
open() returns a file object, and it is that object that has __enter__ and __exit__ methods; see the io.03-May-2017
python - Why can you use open() as context manager?
Stack Overflowhttps://stackoverflow.com › questions
"""

def csv_file():
    ro=data.split('.')
    if [x for x in ro if len(ro)<80]:
        return ro
c = csv_file()
print(c)

def csv_file():
    ro =data.split(',')
    for i in ro:
        if len(ro)<60:
            print(i)
c=csv_file()