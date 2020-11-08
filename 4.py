a=eval(input("introduceti primul numar"))
b=eval(input("introduceti al doilea numar"))
i=0
if a%2==0:
    for i in range(a+1,b,2):
        print(i,end=" ")
else:
    for i in range(a,b,2):
        print(i,end=" ")