def inpu():
    a = []
    for i in range(n):
      l = list(map(int,input().split()))
      a.append(l)
    return a
def verify(a,b):
    for i in range(len(a)):
        if(a[i]>b[i]):
            return False
    return True
n = int(input("enter no of processes : "))
m = int(input("enter no of instances : "))
print("Availble : ")
available = list(map(int,input().split()))
print("Allocation for the resources")
allocation = inpu()
print("Max Resources :")
max = inpu()
need = []
for i in range(n):
    need.append([0]*m)
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j]-allocation[i][j]
print("need : ")
for i in need:
    print(i)
count = 0
done = [False]*n
flag = False
seq = []
while(count<n):
    for i in range(n):
        if(verify(need[i],available) and done[i]==False):
            for j in range(m):
                available[j] += need[i][j]
            done[i] = True
            count += 1
            seq.append('p'+str(i+1))
            flag = True
    if(flag==False):
        break
print(seq)



'''
4
3
2 3 3
2 3 0
1 0 2
3 1 1
2 0 0
7 4 1
2 0 4
4 2 2 
3 2 0
'''