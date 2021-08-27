def knapSack(w, wt, val, n):
    K = [[0 for x in range( w+ 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(w + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][w]

val=list(map(int,input("Enter the values: ").split()))
wt=list(map(int,input("Enter the weights:").split()))
w=int(input("Enter the maximum capacity:"))
n=len(wt)
print(knapSack(w, wt, val, n))


# import numpy as np
# def knapsack(profit,weigths,capacity,n):
#     if(n==-1 or capacity == 0):
#         return 0
#     if(weigths[n]>capacity):
#         return knapsack(profit,weigths,capacity,n-1)
#     else :
#         return max(knapsack(profit,weigths,capacity,n-1),profit[n]+knapsack(profit,weigths,capacity-weigths[n],n-1))
# items = int(input("Enter no of items : "))
# capacity = int(input("Enter Capacity : "))
# pi = list(map(int,input("Enter Profits : ").split()))
# w = list(map(float,input("Enter weights : ").split()))
# print(knapsack(pi,w,capacity,items-1))


# '''
# sample input
# 7
# 15
# 10 5 15 7 6 18 3
# 2 3 5 7 1 4 1

# 3
# 50
# 60 100 120
# 10 20 30

# 5
# 10
# 40 50 100 95 30
# 2 3.14 1.98 5 3
# '''
