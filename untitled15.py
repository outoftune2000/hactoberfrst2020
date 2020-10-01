a =[]
n = int(input("enter the series"))
for i in range(n):
    x = int(input("enter number"))
    a.append(x)
import pickle
c= open("new3.txt","wb")
pickle.dump(a,c)
c.close()
c = open("new3.txt","rb")
x = pickle.load(c)
pos = open("new4.txt","w")
neg = open("new5.txt","w")
for j in x:
    if j >0:
        pos.write(str(j))
    elif j<0:
        neg.write(str(j))
c.close()
neg.close()
pos.close()
pos = open("new4.txt","r")
neg = open("new5.txt","r")
q = neg.read()
k = pos.read()
print("negative",q)
print("posative",k)
        