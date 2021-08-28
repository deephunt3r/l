import sys
p = list(map(int,input("Enter the process names :").split()))
at = list(map(int,input("Enter the arrival time : ").split()))
bt = list(map(int,input("Enter the burst time :").split()))
ct = [0]*len(p)
tat = [0]*len(p)
wt = [0]*len(p)
at_d = at.copy()
bt_d = bt.copy()
v = 0
gant_chart = [0]*len(p)
x = at.index(min(at))

for i in range(len(p)):
     ct[x] = v+bt[x]
     gant_chart[i] = p[x]
     tat[x] = ct[x]-at[x]
     wt[x] = tat[x] - bt[x]
     v = ct[x]
     at[x] = sys.maxsize
     bt[x] = sys.maxsize
     x = bt.index(min(bt))
     m = at.index(min(at))
     if at[x] > v:
        x = m
     else:
        x = bt.index(min(bt))
print("Gantt chart:")
for i in gant_chart:
    print(i,end="|")
print()
    
print("Process   ArrivalTime   BurstTime   CompleteTime   TurnAroundTime  WaitingTime")
for i in range(len(p)):
    print("  ",p[i],"   \t",at_d[i],"   \t",bt_d[i],"\t\t",ct[i],"\t\t",tat[i],"\t\t",wt[i])
print("Average WaitingTime=",sum(wt)/len(wt))
print("Average TurnAroundTime=",sum(tat)/len(tat))

# n = int(input())
# at = list(map(int,input().split()))
# bt = list(map(int,input().split()))
# table = []
# for i in range(n):
#     table.append([0,i,at[i],bt[i]])
# table = sorted(table, key = lambda x:x[2])
# CT = 0
# c = 0
# result = []
# while(c<n):
#     min_list = list()
#     for i in range(n):
#         if(table[i][2]<=CT and table[i][0]==0):
#             min_list.append(table[i])
#     if(len(min_list)==0):
#         CT += 1
#         continue
#     m = min_list[0][3]
#     index = 0
#     for j in range(len(min_list)):
#         if(m>min_list[j][3]):
#             m = min_list[j][3]
#             index = j
#     CT += min_list[index][3]
#     at1 = min_list[index][2]
#     bt1  = min_list[index][3]
#     ct = CT
#     tat = ct-at1
#     wt = tat-bt1
#     p = min_list[index][1]
#     result.append([p+1,at1,bt1,ct,tat,wt])
#     c += 1
#     for i in range(n):
#         if(m==table[i][3] and table[i][0]==0):
#             table[i][0] = 1
#             break
# print("Gantt chart")
# for i in result :
#     print("p"+str(i[0]),end=" ")
# print()
# result = sorted(result,key = lambda x : x[0])
# for i in range(n):
#     print(result[i])


# '''
# 4       
# 0 2 4 5
# 7 4 1 4
# '''


