fc = int(input("enter frames count : "))
fs = int(input("enter size of frame : "))
p = int(input("enter no of pages : "))
ps = list(map(int,input("Enter size of each page : ").split()))
free = list(map(int,input("Enter frames that are free to assign : ").split()))
pagetable = []
s = 0
for i in range(p):
    s += fs-ps[i]
    pagetable.append([i+1,free[i],fs-ps[i]])
for i in pagetable:
    print("page = "+str(i[0])+" frame = "+str(i[1])+" internalfragmentation = "+str(i[2]))
print("Total internal fragementation",s)

'''
8
1024
4
1020 1000 1024 1015
3 0 7 2 5 1
'''
