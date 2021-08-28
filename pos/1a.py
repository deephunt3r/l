print("Enter the process numbers")
pt=list(map(int,input().split()))
print("Enter the arrival time")
at=list(map(int,input().split()))
atd=at.copy()
print("Enter the bursttime")
bt=list(map(int,input().split()))
v=0
ct=[0]*(len(at))
tat=[0]*(len(at))
wt=[0]*(len(at))
gt=[0]*(len(at))
rt=[0]*(len(at))
for i in range(0,len(at)):
    x=at.index(min(at))
    if at[x]>v:
        v=at[x]
    ct[x]=v+bt[x]
    gt[i]=pt[x]
    tat[x]=ct[x]-at[x]
    wt[x]=tat[x]-bt[x]
    rt[x]=v-at[x]
    v=ct[x]
    at[x]=9999

print("Gantt chart:")
for i in gt:
    print(i,end="|")
print()

print("Process   ArrivalTime   BurstTime   CompleteTime   TurnAroundTime  WaitingTime  ResponseTime")
for i in range(0,len(pt)):
    print("  ",pt[i],"   \t",atd[i],"   \t",bt[i],"\t\t",ct[i],"\t\t",tat[i],"\t\t",wt[i],"\t\t",rt[i])
print("Average WaitingTime=",sum(wt)/len(wt))
print("Average TurnAroundTime=",sum(tat)/len(tat))


# n = int(input())
# at = list(map(int,input().split()))
# bt = list(map(int,input().split()))
# table = []
# for i in range(n):
#     table.append([i+1,at[i],bt[i]])
# table = sorted(table, key = lambda x:x[1])
# CT = 0
# c = 0
# while(c<n):
#     if(table[c][1]<=CT):
#         CT += table[c][2]
#         # print(table[c])
#         table[c].append(CT)
#         table[c].append(CT-table[c][1])
#         table[c].append(CT-table[c][1]-table[c][2])
#         c += 1
#     else :
#         CT += 1
# table = sorted(table,key = lambda x:x[0])
# for i in table:
#     print(i)
# print(CT)
