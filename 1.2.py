def inp(row,col):
    a = []
    for i in range(row):
        b = []
        for j in range(col):
            b.append(int(input()))
        a.append(b)
    return a
def mul(x,y,row,col,n):
    a = []
    for i in range(row):
        b = []
        for j in range(col):
            h = 0
            for k in range(n):
               h += x[i][k]*y[k][j]
            b.append(h)
        a.append(b)
    return a
r1 = int(input("enter row size of 1st matrix"))
c1 = int(input("enter column size of 1st matrix"))
print("enter the elements")
a = inp(r1,c1)
r2 = int(input("enter row size of 2nd matrix"))
c2 = int(input("enter column size of 2nd matrix"))
print("enter the elements")
b = inp(r2,c2)
if(r2==c1):
    c = mul(a,b,r1,c2,c1)
    print("After Multiplication")
    print(c)
else :
    print("Addition not Possible")