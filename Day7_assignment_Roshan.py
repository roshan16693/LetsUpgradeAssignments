try:
    file=open("hi.txt","r")
    f=file.read()
    print(f)
except FileNotFoundError:
    print("Something Went Wrong")