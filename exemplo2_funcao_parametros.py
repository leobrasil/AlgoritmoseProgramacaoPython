def addup(first, last):
    if first > last:
        sum = -1
    else:
        sum=0
        for i in range(first,last+1):
            sum=sum+i
    return sum

def addup2(first, last, incr=1):
    if first > last:
        sum = -1
    else:
        sum=0
        for i in range(first,last+1, incr):
            sum=sum+i
    return sum

print(addup(1,10))
print(addup(first=1,last=10))
print(addup(last=10, first=1)) 

print("-----------")

print(addup2(1,10))
print(addup2(1,10,2))
print(addup2(first=1,last=10))
print(addup2(incr=2, last=10, first=1)) 