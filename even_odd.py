l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd_num=[]
even_num=[]
for i in range(len(l)):
    if l[i]%2==0:
        even_num.append(l[i])
    else:
        odd_num.append(l[i])
    
print(odd_num)
print(even_num)


