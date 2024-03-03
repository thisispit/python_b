# lambda arguments : expression

# d = lambda x: x * 2
# print(d(5)) # Prints out 10


# full_name = lambda first, last: f'{first.title()} {last.title()}'

# print(full_name('john', 'doe'))

# a= lambda x,y:x+y
# print(a(10,30))
# # Prints "John Doe"

# x=int(input("Enter the value to be cubed and square: "))
# s= lambda x: x**2
# c= lambda x: x**3
# print("square: " , s(x), "\ncube: " , c(x))


d_list = lambda a:[x*2 for x in a]
print(d_list([1,2,3,4,5,6,7,8,9,10]))

# reverse_list

r_str = lambda a:a[::-1]
print(r_str("hello"))