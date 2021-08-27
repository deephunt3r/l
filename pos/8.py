memory = int(input("Enter memory size : "))
pagesize = int(input("Enter page size : "))
pn = int(input("Enter number of processes : "))
print("Number of pages : ",int(memory/pagesize))
process=[]
l=0
for i in range(pn):
    print("Enter pages for process :",i)
    pg=list(map(int,input().split()))
    l+=len(pg)
    if l<int(memory/pagesize):
        process.append(pg)
    else:
        print("Memory is full")
print("Enter logical address to get pysical address")
pr=int(input("Enter process number :"))
pnum=int(input("Enter page number : "))
offset=int(input("Enter offset : "))
print("pysical address :",(process[pr][pnum])*pagesize+offset)
