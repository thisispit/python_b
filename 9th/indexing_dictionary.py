# my_dict={'name':'pitamber',
#          'age': 20,
#          'city':'Osaka',
#          'job':'Engineer'}

# my_dict={'name':'piyush',
#          'age': 21,
#          'city':'New York',
#          'job':'Engineer'}

# #adding a new key value pair
# my_dict['gender']='male'

# #updating the value of an existing 
# my_dict['age']=26

# #checking if a key exist
# if 'city' in my_dict:
#     print(f"City: {my_dict['city']}")


# a={1,2,3,4,5,6,7,8}
# #print my set on counsole
# print(a)
# #print type of a
# print(type(a))
# #print length of my set
# print(len(a))


# a={'apple':2,'banana':4,'cherry':6}

# #iterating through key-value pairs
# # for fruit,quantity in a.items():
# #     print(f"there are {quantity} {fruit}s.")

# for fruit in a:
#     a[fruit]*=2

# print(a)


# to make all the world in lower case
# text="Hello,World!"
# lcase_text=text.lower()
# print(lcase_text)

# to make all in upper case
# text="hello,world!"
# ucase_text=text.upper()
# print(ucase_text)


#to capatilized words
# text="hello,world!"
# capitalize_text=text.capitalize()
# print(capitalize_text)

#titile() is used to capatilized the first letter of every word
# text="hello,world!"
# title_text=text.title()
# print(title_text)


#its used to count the no of occurance of word
# text="hello,world!,hello"
# count_text=text.count("hello")
# print(count_text)


# text="hello,world!"
# index=text.find("world")
# print(index)



# text="hello,world!"
# new_text=text.replace("hello", "hi")
# print(new_text)


# text="hello,world!"
# capitalize_text=text.capitalize()
# print(capitalize_text)


# text="hello,world!"
# starts_with=text.startswith("hello")
# ends_with= text.endswith("hello")
# print(starts_with,ends_with)


fruits_list=['apple','orange','banana']
text= ",".join(fruits_list)
print(text)