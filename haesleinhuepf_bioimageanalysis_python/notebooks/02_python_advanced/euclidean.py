import math

def euc_dist(p, q):
    s = 0

    for a,b in zip(p, q): 
        s = s + a*b
    return math.sqrt(s)