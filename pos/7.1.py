m = int(input("enter total memory : "))
p = []
pi = 1
while(1):
    pm =int(input("enter the memory required for process "+str(pi)+" : "))
    if(pm<m):
        p.append(pm)
        pi += 1
        m -= pm
        n = int(input("1.continue\n2.Exit\n"))
        if(n==1):continue
        else : break
    else : 
        print("cannot allocate")
        break
for i in range(len(p)):
      print("process "+str(i+1)+" allocated memory = "+str(p[i]))
print("External Fragmentation = "+str(m))
print("Total memory = "+str(sum(p)))

'''
1200
350
1
283
1
435
1
200

'''