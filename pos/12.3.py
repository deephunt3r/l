n = int(input("no of tracks : "))
a = list(map(int,input("Enter request queues : ").split()))
head = int(input("read head : "))
d = input("Enter direction left or right: ")
R = sorted([i for i in a if i>head])
L = sorted([i for i in a if i<head])
if(d == "right"):
    print("Sequence : ",R+L)
    print(n-head+n+max(L))
else :
    print("Sequence : ",L[::-1]+R[::-1])
    print(head+n+n-min(R))
'''
199
82 170 43 140 24 16 190
50
right
'''
