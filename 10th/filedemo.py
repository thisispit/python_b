# filedemo=open("tsr.txt","a")

# filedemo.write("Hello from vs code\n")
# filedemo.write("hello world ")
# filedemo.close


# if filedemo:
#     print("file is open")
# else:
#     print("file is not open")

# with open("tsr.txt","r")as f:
#     data=f.read()
#     print(data)

# f=open("tsr.txt","a")
# f.write("\n Delhi is a smart city" )
# f.close()
# print("file operation is done")


f=open("tsr.txt","r")
print("current indeex position of file pointer",f.tell())
print(f.read())
f=open("tsr.txt","a")
f.write("\n Delhi is a smart city" )
f.close()
print("file operation is done")

