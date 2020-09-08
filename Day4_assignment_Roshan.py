low=1024000
upper=7024000

for i in range(low,upper+1):
    temp=i
    result=0
    while temp>0:
        fir=temp%10
        result+=fir**len(str(i))
        temp=temp/10
    if(i==result):
        print("Got it",i)
        break