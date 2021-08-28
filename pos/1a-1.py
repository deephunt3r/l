n = int(input())
at = list(map(int,input().split()))
bt = list(map(int,input().split()))
table = []
for i in range(n):
    table.append([i+1,at[i],bt[i]])
table = sorted(table, key = lambda x:x[1])
CT = 0
c = 0
while(c<n):
    if(table[c][1]<=CT):
        CT += table[c][2]
        # print(table[c])
        table[c].append(CT)
        table[c].append(CT-table[c][1])
        table[c].append(CT-table[c][1]-table[c][2])
        c += 1
    else :
        CT += 1
table = sorted(table,key = lambda x:x[0])
for i in table:
    print(i)
print(CT)
