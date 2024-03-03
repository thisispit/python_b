""" 
# 1) len() 

my_list=[1,2,3,4,5]
length=len(my_list)
print(f"length of my_list: {length} ")

index no and no of element are two different things
we get there class with function  type()
we get id (index no) with id()



2) max()
these are inbuilt function which gives max output of a particular list

my_list=[1,2,3,4,5]
print(max(my_list))


3) min()
these are inbuilt function which gives min output of a particular list

my_list=[1,2,3,4,5]
print(min(my_list))


4) sorted()
to get ans in order of in sorted (ascending or descending) order

a,b,c = map(int, input("Enter three numbers: ").split(','))
print(a,b,c)


5) .instert

my_list=[1,2,3,4,5]
my_list.insert(2,10)
print(my_list)

6) .remove


my_list=[1,2,3,3,4,5,5]
my_list.remove(3)
my_list.remove(3)
print(my_list)


my_list=[1,2,3,3,4,5,5]

for index, v in enumerate(my_list):
    print(f"index: {index}, valur:{v}")

    


matrix_3x3=[
    [1,2,5],
    [3,4,4],
    [2,3,4]
]

for row in matrix_3x3:
    print(row)

    
7) zip()

we use zip  function of we want to use the all the vairable of the list all in one time


matrix_3x3=[
    [1,2,5],
    [3,4,4],
    [2,3,4]
]
for col in zip(*matrix_3x3):
    print(col)

    
9)combining Positve and Negative Indexing:
my_tuple=(1,2,3,4,5)
mixed_indexing=my_tuple[::-1]
print(f"Mixed_indexing: {mixed_indexing}")
10) absic for loop:


list=(1,2,3,4,5)
for element in list:
    print(element)

11) printing list using while loop

my_tuple=(1,2,3,4,5)
index=0
while index< len(my_tuple):
    print(my_tuple)
    index+=1

    

#taking input as tuple
user_input=input("enter element for the tuple seperated by space: ")

#splitting the input string into a list of strings
elements= user_input.split()

#converting the list of string into a tuple
my_tuple=tuple(elements)
print(f"tupke: {my_tuple}")


""" """
#taking input for a 2x3 nested tuple
rows=2
column=3

nested_tuple=[]

for i in range(rows):
    inner_tuple=tuple(input(f"Enter elements for row {i+1} seperated by space: ").split())
    nested_tuple.append(inner_tuple)

#diaplaying nested tuple
print("Nested tuple: ")
print(nested_tuple)


rows=int(input("Enter the number of rows in the matrix: "))
column=int(input("Enter the number of column in a matrix: "))

matrix=[]

#taking input for each row
for i in range(rows):
    row_input=input(f"Enter elements for row {i+1} seperated by space: ").split()
    row_element= tuple(map(int,row_input.split()))
    matrix.append(row_element)

#displaying the matrix
print("Matrix: ")
for row in matrix:
    print(row)

 

# clear method
newset={"apple","banana","cherry"}
newset.clear()
print(newset)


# delete del()
n={"apple","banana","cherry"}
del n
print(n)


# union() method returns a new set with all items from both sets

set1={"a","b","c"}
set2={1,2,3}

set3= set1.union(set2)
print(set3)


#update()

set1={"a","b","c"}
set2={1,2,3}

set3= set1.update(set2)
print(set3)


# intersaction() it jjst pick pout the common element between lists
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}

x.intersection_update(y)
print(x)


#dictionary()

dictionary= {1:'Rahul',2:'Bhavesh',3:'Akhilesh',4:'shashank'}

print(dictionary)

print("1st name:"+dictionary[1])
print("4st name:"+dictionary[4])

print(dictionary.keys())
print(dictionary.values())


# lower()
text="hello,world!"
lcase_text=text.lower()
print(lowercase_text)

# upper()

# capatilized()
# text="hello,world!"
# capitalize_text=text.capitalize()
# print(capitalize_text)


# count()

"""
"""

gender=my_dict.get('gender','not specified')
weuse it to call and edit the value of it






assignment:
book management system
1) add book
2) display book
3) delete book
4) update book
5) exit


"""