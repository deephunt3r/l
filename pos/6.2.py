def worstfit(b,p,m,n):
    assigned = [-1]*n
    for i in range(n):
        maxi = max(b)
        index = b.index(maxi)
        if(b[index]<p[i]):
            continue
        b[index] -= p[i]
        assigned[i] = index

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
worstfit(b,p,m,n)