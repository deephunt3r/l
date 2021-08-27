def firstfit(b,p,m,n):
    assigned = [-1]*n
    for i in range(n):
        for j in range(m):
             if(p[i]<b[j]):
                 b[j] -= p[i]
                 assigned[i] = j
                 break
    print("ProcessNo","\t","PM","\t","Block Address") 
    for i in range(n): 
        print("Process "+str(i),"\t",str(p[i]),"\t",end=" ")  
        if(assigned[i] != -1):  
            print("Block "+str(assigned[i]))
        else: 
            print("NA")
m = int(input("enter no of blocks in memory : "))
n = int(input("enter no of proceses: "))
b = list(map(int,input("enter blocks memory : ").split()))
p = list(map(int,input("enter process memory : ").split()))
firstfit(b,p,m,n)