def bestfit(b,p,m,n):
    assigned = [-1]*n
    for i in range(n):
        mini = max(b)
        index = b.index(mini)
        for j in range(m):
            if(mini>b[j] and b[j]>p[i]):
                mini = b[j]
                index = j
        # if(b[index]<p[i]):
        #     continue
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
bestfit(b,p,m,n)