
def getinput(func):
    def wrapper(num):
        for i in range(1,num):
            if i%2==0:
                print(i)
        return func(num)
    return wrapper

@getinput
def putinput(num):
    return num

print(putinput(10))



try:
    file=open("hi.txt","r")
    f=file.read()
    print(f)
except FileNotFoundError:
    print("Something Went Wrong")