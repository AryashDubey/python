def fibonacci(n):
    a=[]
    for q in range(n):
        if(q==0):
            a.append(0)
        elif(q==1):
            a.append(1)
        else:
            a.append(a[-1]+a[-2])
    print(a)
fibonacci(5)
