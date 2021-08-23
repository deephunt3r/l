import math
items = int(input("Enter no of items : "))
item = list(i for i in range(1,items+1))
capacity = int(input("Enter Capacity : "))
pi =list(map(int,input("Enter Profits : ").split()))
w =list(map(float,input("Enter weights : ").split()))
p_ratios = []
table = []
for i in range(items):
  p_ratios.append((pi[i]/w[i]))
  table.append((item[i],w[i],pi[i],p_ratios[i]))
table = sorted(table,key=lambda x:x[3],reverse=True)
tp = 0
items_selected = list()
if(items==0 or capacity == 0):
  print("Incorrect data")
for i in range(items):
  if(table[i][1]<=capacity):
    capacity-=table[i][1]
    tp+=table[i][2]
    items_selected.append([table[i][0],1])
  else:
    tp+=((capacity/table[i][1])*table[i][2])
    items_selected.append([table[i][0],capacity/table[i][1]])
    break
items_selected = sorted(items_selected,key=lambda x:x[0])
print("Item Fraction")
for i in items_selected :
    for j in i:
        print(" "+str(j),end="\t")
    print()
print("Total Profit = ",tp)


'''
4
6
15 20 30 14
3 2 10 2
'''