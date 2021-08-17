""" A program is sentence that all the letter of the English alphbet atleast once
 for example,

The quick brown Jumps over the lazy dog
your task here is to write a function to check a sentence to see if it is panagram or not.

Coding:-

"""
def panagram(nt):
    check="abcdefghijklmnopqrstuvwxyz"
    for l in check:
        if l in nt:
            continue
        else:
            return False

    return True

n=input("Enter Any Text:")
if(panagram(n.lower())):
    print("Yes It is a prangram")
else:
    print("No It is not a panagram")

