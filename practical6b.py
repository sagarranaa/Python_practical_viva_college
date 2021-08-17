"""
Write a Python program to append text to a file and display the text
Code:-
"""
def main():
    f=open("text.txt","a+")
    f.write("Welcome to workshop on Python")
    f.close()
if __name__=="__main__":
    main()