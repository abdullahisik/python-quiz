import sys
import numpy as np

array = np.array([])
chars = list()
char = ''
def strPattern(mystr):
    mystr = mystr.upper()
    liste =list(mystr)
    print(liste)
    uzunluk = len(mystr)*2-1
    for x in range(0, len(mystr)):
        chars.append(liste[x])
        if x+1 < len(mystr):
            b = str(x+1)
            chars.append(b)        
    str1 = ""
    print(str1.join(chars))
strPattern('Burkay')