def seq():
    n = int(input("no of files to be allocated : "))
    for i in range(n):
        s,l = map(int,input("enter the starting block and length of file"+str(i+1)+" : ").split())
        count = 0
        for j in range(s,s+l):
            if(blocks[j] == 0):
                count += 1
        if(count == l):
            print("for file "+str(i+1))
            for j in range(s,s+l):
                blocks[j] = 1
                print("block "+str(j)+" is allocated")
        else:
            # for i in range(bs):
            #  print(i,blocks[i])
            print("cannot allocate for file "+str(i+1))

bs = int(input("number of blocks : "))
m = int(input("enter no of blocks that are already filled : "))
mf = list(map(int,input("enter the block numbers : ").split()))
blocks = [0]*bs
for i in mf:
    blocks[i] = 1

seq()
 
'''
20
5
2 6 10 14
3
0 2
7 5
16 3

'''