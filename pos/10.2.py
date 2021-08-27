def indexed():
    n = int(input("no of files to be allocated : "))
    for i in range(n):
        ind,l = map(int,input("enter the index block and length of file "+str(i+1)+" : ").split())
        if(blocks[ind]==None):
            count = 0
            blocks[ind]= []
            for j in range(bs):
                if(blocks[j]==None):
                    blocks[j] = 1
                    blocks[ind].append(j)
                    count += 1
                if(count==l):
                    break
            print("File"+str(i+1)+" allocated with index "+str(ind)+" and block numbers = ",blocks[ind])   
        else :
            print("cannot be allocated for file "+str(i+1))
    return

bs = int(input("number of blocks : "))
m = int(input("enter no of blocks that are already filled : "))
mf = list(map(int,input("enter the block numbers : ").split()))
blocks = [None]*bs
for i in mf:
    blocks[i] = 1
indexed()

'''
20
5
2 5 9 13 17
3
1 4
2 3
10 3

'''