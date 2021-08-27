m = int(input("enter total available memory : "))
bs = int(input("enter the block size : "))
n = int(input("enter the no of process : "))
i_f = []
p = []
for i in range(n):
    s = int(input("enter size of process "+str(i)+" : "))
    if(s<=bs):
       i_f.append(s)
       p.append(i)
inf = 0
for i in range(n):
    if i in p:
        index = p.index(i)
        print("process "+str(i)+" has been allocated of memory "+str(i_f[index])+" with internal fragmentation "+str(bs-i_f[index]))
        inf += bs-i_f[index]
    else:
        print("process "+str(i)+" cannot be allocated")
print("External fragmentation = "+str(m-sum(i_f)-inf))
print("Internal fragmentation = "+str(inf))

'''
1800
375
6
290
480
710
222
353
111
'''
