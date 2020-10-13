from inverseField import inverseField
from mul_field import mul_field

def div_field(mod,f,a,b):
    multINV=inverseField(mod,f,b)
    if (multINV=='ERROR'):
        return 'ERROR'
    else:  
        return mul_field(mod,f,a,multINV)
    
(div_field(2,[1,0,1,1],[1,0],[1,1,1]))    