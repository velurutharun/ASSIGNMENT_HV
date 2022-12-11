s=open("carprogramm.txt","a")
car={}
for i in range(5):
    b=input("Enter the brand name: ")
    car[b]=input("Enter the color: ")
print(car)
print(car,file=s)
s.close()