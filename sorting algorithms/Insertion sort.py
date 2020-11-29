
#insersion sort -forloop

a=[]
b=int(input())
for i in range(0,b):
    temp=int(input())
    a.append(temp)
    for j in range(0,len(a)):
        if(a[j]>a[i]):
            a[j],a[i]=a[i],a[j]
print(a)

#insrsion sort  -while loop

for i in range(0,b):
    j=0
    while(j>=0 and j<=len(a) and a[i]>a[j]):
        a[j],a[i]=a[i],a[j]
        j+=1
print(a)

#for both programs the insersion sort is O(n^2)
