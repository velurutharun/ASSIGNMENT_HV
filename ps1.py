x=open("sumdata.txt","a")
a=[]
for i in range(5):
    b=int(input("Enter the number:"))
    a.append(b)
print("The numbers are: ",a)
print("The numbers are ",a,file=x)
print("sum of numbers: ",sum(a))
print("sum of numbers: ",sum(a),file=x)