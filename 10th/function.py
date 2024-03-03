""" 

#filedemo()


filedemo.write()
filedemo.open()
filedemo.close()

used to modify a file

        #access modes are:
"r" is used for reading text files
"w" overwrites existing files or creates new
"a" is useful for appending to log files
"r+" allows both reading and writing 


with statement 

with statement is useful in manupulation a file 

with open(<filename>,<access mode>)as <filepointer>


#fileptr.writr("python is th emodern prigramming language")

fileptr.close()


mylist=[...]
f.writelines(mylist)
f.close()


f=open("myfile.txt","r")
print("current indeex position of file pointer",f.tell())
print(f.read())


"""