# 1) abs() function

""" 
i=-20
print(abs(i))
e=-20.34
print(abs(e))
f=str("20")
f=int(f)
print(abs(f))
 """

# 2) all() function

""" k=[1,2,3,4,5,66,7,7,8,]
print(all(k))

i=[0,False]
print(all(i)) """

# 3) exec() function (execution)

""" x=int(input("enter value: "))
exec('print(x==8)')

exec('print(x%2)')
if x==0:
    print("even")
else:
    print("odd")

exec('print(x+4)') """

# 4) sum() function

""" a=sum([1,2,3,4,5,6,7,8,9,10,11])
print(a)

b=[1,2,3,4,5,6,7,8,9,10,11]
print(sum(b)) """

# 5) any() function

i=[4,3,21]
print(any(i))

i=[]
print(any(i))

i=[0,True]
print(any(i))



# 6) ascii() function

t="Python is intresting"
print(ascii(t))





# 7) eval() function



# 8) float() function



# 9) format() function

print(format(123,"d"))

# 10) frozenset() function

# 11) getattr() function



# 12) append()
name=["pit"]
list2=["new"]
list1=["is","or","am"]
list1.append("the")
print(list1) #append=add it add at the last
list1[2]="is"
print(list1)
list1.insert(3,"ABC") #it inserts the data at the 3rd position and else remain same 
print(list1)
list1.remove("ABC")
print(list1)
list1=name.copy
print(list2)