n1=int(input("introduceti primul numar"))
n2=int(input("introduceti al doilea numar"))
n3=int(input("introduceti al treilea numar"))
n4=int(input("introduceti al patrulea numar"))
n5=int(input("introducati al cincilea numar"))
n6=int(input("introduceti al saselea numar"))
i=0
s1=0
s2=0
s3=0
s4=0
s5=0
s6=3
for i in range(1,n1+1):
    s1+=i
for i in range(2,n2+1):
    s2+=(i-1)*i
for i in range(1,n3+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s3+=p
for i in range(1,n4+1):
    s4+=i*10+2
for i in range(1,n5+1):
    s5+=i/(i+1)
for i in range(2,n6+1):
    if i<10:
        s6+=20+i
    else:
        s6+=20*(10**(i//10))+i
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)