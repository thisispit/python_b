""" l=["a","b","c","d","e","f","g"]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[-2])
print(l[-1])
print(l[2:5]) #n=5 n-1=4
print(l[:5])
print(l[1:6:2])
print(l[0:7:2])


print(list1[1:8:2])
list1[5]=100
print(list1) """


list1=[1,2,3,4,5,6,7,8,9,10]
z=int(input("enter no to search: "))
if z in list1:
    print("number is available")
else:
    print("number not available")