def wait(s):
    return s-1
def signal(s):
    return s+1
mutex = 1
s = int(input("enter buffer size : "))
empty = s
buffer = [0]*s
full = 0
while(1):
    print("0.exit\n1.producer\n2.consumer")
    n = int(input())
    if(n == 1):
        #producer code
        if(empty!=0 and mutex==1):
            empty = wait(empty)
            mutex = wait(mutex)
            n = int(input("Enter a number to produce : "))
            buffer[full] = n
            mutex = signal(mutex)
            full = signal(full)
        else :
            print("It is full ")
    elif(n == 2):
        #consumer code
        if(full!=0 and mutex==1):
            full = wait(full)
            mutex = wait(mutex)
            print("consumed ",buffer[full])
            mutex = signal(mutex)
            empty = signal(empty)
        else:
            print("It is empty")
    else :
        exit(0)
            
