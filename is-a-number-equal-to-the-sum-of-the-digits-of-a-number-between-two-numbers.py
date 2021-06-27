import math

def sumDigits(f,t,x):
    if f>t:
        if t>=10:
            r=math.floor(t/10)
            t=x-r
            t=t+r*10
            if(t<=f):
                print(t)
            else:
                return -1
        else:
            return -1    
    else:
        if f>=10:
            r=math.floor(f/10)
            f=x-r
            f=f+r*10
            if(f<=t):
                print(f)
            else:
                return -1
        else:
            return -1    
sumDigits(25,20,9)