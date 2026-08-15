#make a computer program that returns FLOPs
#the algorithm

import math

def main(x):
    #Step 1A: Determine the Sign Bit(s)
    if x < 0:
        s = 1
    else:
        s = 0
    
    #Step 1B: Convert Decimal to Binary

    integer = math.floor(x)
    print(integer)



main(3.14159)
