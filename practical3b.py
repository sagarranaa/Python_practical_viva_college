"""
Take a list ,say for an example this one: a=[1,1,2,3,5,8,13,21,34,55,89] and write a program
that prints out all the elements of the list that are less than 5
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
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))




