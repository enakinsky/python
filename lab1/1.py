def delit(x):
    counter = 0
    for i in range(2,x+1):
        if(x%i==0):
            if(i%3==0):
                counter += 1
    return counter
