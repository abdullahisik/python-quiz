import math
class corner:
    def _init_(self, x, y):
        self.x = x
        self.y = y
def intersection(l1,b1,r1,t1,l2,b2,r2,t2):
    lb1 = corner(l1,b1)
    rt1 = corner(r1, t1)
    lb2 = corner(l2,b2)
    rt2 = corner(r2, t2)
    intr1 = min(rt1.x, rt2.x) - max(lb1.x, lb2.x)
    intr2 = min(rt1.y, rt2.y) - max(lb1.y, lb2.y)
    if intr1>=0 and intr2>=0:
        return 2*(intr1*intr2)
print(intersection(0,0,5,5,3,3,7,7))