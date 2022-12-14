x=open("sumdata.txt","a")
b=[]
for i in range(5):
    a=int(input("enter  a number: "))
    if a>0:
        b.append(a)
    else:
        break
if len(b)==5:
    print(b)
    print(sum(b))
else:
    print("please enter all positive numbers as input")