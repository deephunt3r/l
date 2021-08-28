def linked():
    n = int(input("no of files to be allocated : "))
    for i in range(n):
        start,l = map(int,input("enter the index block and length of file "+str(i+1)+" : ").split())
        if(blocks[start]==None):
            count = 0
            trav = start
            for j in range(bs):
                if(blocks[j] == None and j!= start):
                    blocks[trav] = j
                    trav = j
                    count += 1
                if(count==l):
                    break
            t = start
            print("blocks "+str(t)+" --> ",end=" ")
            for k in range(l-1):
                print(str(blocks[t])+" --> ",end=" ")
                t = blocks[t]
            print("End allocated for file "+str(i+1))
        else :
            print("cannot be allocated for file "+str(i+1))
bs = int(input("number of blocks : "))
m = int(input("enter no of blocks that are already filled : "))
mf = list(map(int,input("enter the block numbers : ").split()))
blocks = [None]*bs
for i in mf:
    blocks[i] = 1
linked()
'''
20
5
2 6 9 13 18
3
4 3
1 4
10 2

'''
