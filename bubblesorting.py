l=[1,2,5,4,8,8,89,0]
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            
print(l)