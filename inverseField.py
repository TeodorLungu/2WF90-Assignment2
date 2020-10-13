
from extended_eulclid import extended_euclid

def inverseField(mod,d,a):
    output = extended_euclid(mod,a,d)
    if output[3]==[1]:
        return output[4]
    else:
        return "ERROR"

(inverseField(2,[1,1,0],[0]))        