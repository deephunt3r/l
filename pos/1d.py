print("Enter the process numbers")
pt=list(map(int,input().split()))
print("Enter the arrival time")
at=list(map(int,input().split()))
print("Enter the bursttime")
bt=list(map(int,input().split()))
print("Enter the priority")
pq=list(map(int,input().split()))
pqd=pq.copy()
v=0
ct=[0]*(len(at))
tat=[0]*(len(at))
wt=[0]*(len(at))
gt=[0]*(len(at))
rt=[0]*(len(at))
x=at.index(min(at))
flag=0
for i in range(0,len(at)):
    if at[x]>v:
        flag=1
        pr=min(pq)
        x1=x
        pq[x1]=9999
        x=pq.index(min(pq))
    ct[x]=v+bt[x]
    gt[i]=pt[x]
    tat[x]=ct[x]-at[x]
    wt[x]=tat[x]-bt[x]
    rt[x]=v-at[x]
    v+=bt[x]
    pq[x]=9999
    x=pq.index(min(pq))
    if flag==1:
        pq[x1]=pr
        x=pq.index(min(pq))
        flag=0

print("Gantt chart:")
for i in gt:
    print(i,end="|")
print()

print("Process   Priority  ArrivalTime   BurstTime   CompleteTime   TurnAroundTime  WaitingTime  ResponseTime")
for i in range(0,len(pt)):
    print("  ",pt[i],"   \t",pqd[i],"   \t",at[i],"\t\t",bt[i],"\t   ",ct[i],"\t\t",tat[i],"\t\t",wt[i],"\t   ",rt[i])
print("Average WaitingTime=",sum(wt)/len(wt))
print("Average TurnAroundTime=",sum(tat)/len(tat))

# n = int(input())
# at = list(map(int,input().split()))
# bt = list(map(int,input().split()))
# pr = list(map(int,input().split()))
# table = []
# for i in range(n):
#     table.append([0,i,at[i],bt[i],pr[i]])
# result = []
# c = CT = 0
# while(c<n):
#     min_list = []
#     for j in range(n):
#         if(table[j][2]<=CT and table[j][0]==0):
#             min_list.append(table[j])
#     if(len(min_list)==0):
#         CT += 1
#         continue
#     m = min_list[0][4]
#     index = 0
#     for i in range(len(min_list)):
#         if(m>min_list[i][4] ):
#             m = min_list[i][4]
#             index = i
#     CT += min_list[index][3]
#     bt1 = min_list[index][3]
#     at1 = min_list[index][2]
#     pr1 =  min_list[index][4]
#     p = min_list[index][1]+1
#     ct = CT
#     tat = ct-at1
#     wt = ct-bt1
#     result.append([p,at1,bt1,pr1,ct,tat,wt])
#     for i in range(n):
#         if(m==table[i][4] and table[i][0]==0):
#             table[i][0] = 1
#     c += 1
# print("Ganttchart : ")
# for i in result:
#     print("p"+str(i[0]),end = " ")
# print()
# result = sorted(result,key = lambda x: x[0])
# for i in result:
#     print(i)
