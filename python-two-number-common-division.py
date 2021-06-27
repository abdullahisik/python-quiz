import math

def notRelprime(a,b):
    if a != 1 and b != 1:
        if a%1==a%2==0 and b%1==b%2==0 or b%a == 0 or a%b == 0:
            print("true")
            return True
        else:
            print("false")
            return False
    else:
        print("false")
        return False
notRelprime(3,7)