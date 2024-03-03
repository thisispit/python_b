n=10
n1=0
n2=1
nxt_num=n2
count=1

while count<=n:
    print(nxt_num, end=" ")
    count +=1
    n1,n2=n2,nxt_num
    nxt_num=n1+n2
print()