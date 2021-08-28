p = list(map(int,input("Enter the processes : ").split()))
at = list(map(int,input("Enter the arrival times").split()))
bt = list(map(int,input("Enter the burst time : ").split()))
t = int(input("Enter the time quanttum : "))
at_s = sorted(at)
bt_c = bt.copy()
ct = [0]*(len(p))
tat = [0]*(len(p))
wt = [0]*(len(p))
rt = [0]*(len(p))

gantt_chart = []
ready_queue = []

val = cnt = flag = i = 0
s = sum(bt)+min(at)
while max(ct) != s:
    while i < len(at_s) and val >= at_s[i]:
        ready_queue.append(at_s[i])
        i+=1
    
    if flag == 1:
        ready_queue.append(at[x])
    
    x = at.index(ready_queue[0])
    if p[x] not in gantt_chart:
        rt[x] = val - at[x]
    gantt_chart.append(x)
    ready_queue.remove(at[x])
    
    if bt[x] <= t and bt[x] != 0:
        ct[x] = bt[x]+val
        tat[x] = ct[x]-at[x]
        wt[x] = tat[x] - bt_c[x]
        val += bt[x]
        bt[x] = 0
        flag = 0
        
    else:
        bt[x] = bt[x]-t
        val+=t
        flag = 1

print(ct)
print(tat)
print(wt)
print(rt)
print(gantt_chart)

'''
0 1 2
0 2 4
7 4 1
3
'''