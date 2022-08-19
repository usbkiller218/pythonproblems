#prime number check
a=int(input("enter a number"))
cont=0
for i in range(2,a):
    if a%i==0:
        cont+=1


if cont==0:
    print("prime")
else:
    print("not ar prime ")

