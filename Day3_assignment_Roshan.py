# Pilot Program -- Day3 assignment 1
altitude=int(input("Enter The Current Altitude"))
if altitude<=1000:
    print("Safe To Land")
elif altitude>1000 and altitude<5000:
    print("Bring Down To Less Than 1000ft Altitude")
else:
    print("Has To Make A Turn Around")


# Prime Number Program -- Day3 assignment 2

for i in range(2,200):
    is_Prime=True
    for j in range(2,i):
        if i%j==0:
            is_Prime=False
    if is_Prime:
        print(i)

print(4%3)