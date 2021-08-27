import sys
def order(s,i,j,n):
    if s[i][j] != 0:
        print("(",end = " ")
        order(s,i,s[i][j],n)
    if s[i][j] == 0:
        if i==n-1 and j==n-1 :
            print("M"+str(n-1),end=" ")
        else:
            print("M"+str(s[i][j+1]),end=" ")
        if s[i][j] != 0:
            order(s,s[i][j]+1,j,n)
            print(")",end= " ")
def matrix_chain(d,n):
    m = [[0 for i in range(n)] for i in range(n)]
    s = [[0 for i in range(n)] for i in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i+l-1
            m[i][j] = sys.maxsize
            for k in range(i,j):
                min = m[i][k]+m[k+1][j]+(d[i-1]*d[j]*d[k])
                if min < m[i][j]:
                    m[i][j] = min
                    s[i][j] = k
    print("Maximum size in matrix :",m[1][n-1])
    order(s,1,n-1,n)

n = int(input("Enter no of matrices : "))
dimenssions = []
for i in range(n):
x = list(map(int,input().split()))
dimenssions.append(x[0])
dimenssions.append(x[1])
print(dimenssions)
matrix_chain(dimenssions,len(dimenssions))
