sublist=[1,1,5]
listy=[1,4,5,6,1,3,4,11,7,35]
check=[]
for i in sublist:
  for j in listy:
    if i==j:
      check.append(j)
      listy=listy[listy.index(j)+1:]
      break
if sublist==check:print("It's a Match")
else: print("It's Gone")



lists=["hey this is sai","i am in mumbai","where are you from","i am from thane"]
newl= list(map(lambda name: name.title(),lists))
print(newl)



def prime(primea):
    for i in range(2,primea):
        if primea%i==0:
            return False
    return True

l=filter(prime,range(2500))
print(list(l))