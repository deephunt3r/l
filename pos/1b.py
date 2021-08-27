n = int(input())
at = list(map(int,input().split()))
bt = list(map(int,input().split()))
table = []
for i in range(n):
    table.append([i,at[i],bt[i]])
table = sorted(table, key = lambda x:x[2])
CT = 0
c = 0
while(c<n):
    min_list = list()
    for i in range(n):
        if(table[i][1]<=CT):
            min_list.append(i)
    m = min_list[0]
    CT += table[m][2]
    table[c].append(CT)
    table[c].append(CT-table[c][1])
    table[c].append(CT-table[c][1]-table[c][2])
    c += 1
for i in range(n):
    print(table[i])