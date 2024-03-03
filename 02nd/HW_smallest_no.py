a=float(input("enter 1st number: "))
b=float(input("enter 2nd number: "))
c=float(input("enter 3rd number: "))

if (a<b and a<c ):
    #print(a,"is smallest")
    smallest=a

elif (b<a and b<c):
    #print(b, " is the smallest")
    smallest=a

else:
    #print(c,"is smallest")
    smallest=c

print(smallest, "is the smallest")