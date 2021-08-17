"""
Write a python scipt to sort (ascending and Descending ) a dictionary by value
Coding:-
"""
released={"Python 3.6":2017,"Python 1.0":2002,"Python 2.3":2010}
print("Original dictionary :",released)
print("Dictionary in ascending order by values :")
for key,value in sorted(released.items()):
    print(key,value)
print("Dictionary in Descending order by value :")
for key,value in sorted(released.items(),reverse=True):
    print(key,value)