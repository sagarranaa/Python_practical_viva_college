"""
Write a Python program to read an entire text file
Coding:-
"""
def file_read(fname):
    from itertools import islice
    with open(fname,"w")as myfile:
        myfile.write("Python Exercies\n")
        myfile.write("Java Exercise")
    txt=open(fname)
    print(txt.read())
file_read('abc.txt')