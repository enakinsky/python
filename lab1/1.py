def delit(x):
    counter = 0
    for i in range(2,x+1):
        if(x%i==0):
            if(i%3==0):
                counter += 1
    return counter
-------------------------------
def min(x):
    y = x
    last = x
    while y > 0:
        last1 = y % 10
        if (last1%2==1):
            if last1 < last:
                last = last1
        y = y // 10
    if(last == x):
        return print("does not exist")
    else:
        return last
