a = list(map(int,input("Enter request queues : ").split()))
head = int(input("read head : "))
h = head
sum = 0
for i in a:
    if(i>head):
        sum += i-head
    else :
        sum += head-i
    head = i
print("sequence : ",[h]+a)
print(sum)