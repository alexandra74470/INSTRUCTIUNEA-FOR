n=int(input("introduceti un numar"))
s=0
i=0
for i in range(1,n,1):
    if ((i%3==0)or(i%5==0)):
        s+=i
print("Suma este",s)