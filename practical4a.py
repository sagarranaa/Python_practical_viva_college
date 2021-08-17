"""
4.a)write a program that takes list and returns True if they have at least one common member
Coding:-
"""
def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
    return result
print(common_data([1,4,78,5],[5,4,778,5]))
print(common_data([7,4,8,27,5],[7,4,27,2,7]))