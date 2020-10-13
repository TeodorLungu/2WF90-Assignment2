from div_field import div_field

def equals_field(mod,f,a,b):
    if (div_field(mod,f,a,b)[1]==[1]):
        return True
    else:
        return False    

print(equals_field(5,[1,0,2],[1,0,0],[3]))