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

