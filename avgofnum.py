a=int(input("Enter number of elements:-"))
l=[]
for i in range(a):
    b=(int(input("Enter element;- ")))
    l.append(b)

c=sum(l)/a
print("The avg of given numbers is:-",c)
    