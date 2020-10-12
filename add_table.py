from variousFunctions import elim_lead_zeros
from display_poly import display_poly
from variousFunctions import deg
from variousFunctions import reduction
from generateFF import generate_ff
from add_poly import add_poly
from longdivision import long_div_poly
import math as m

def add_table(mod,f):
    size=int(m.pow(mod,deg(f)))
    Matrix= [[0 for x in range(size)] for y in range(size)]
    MatrixPretty = [['0' for x in range(size)] for y in range(size)] 
    Field=generate_ff(mod,f)[1]
    for i in range(size):
        for j in range(size):
            Matrix[i][j]=add_poly(mod,Field[i],Field[j])[1]
            Matrix[i][j]=long_div_poly(mod,Matrix[i][j],f)[3]
            MatrixPretty[i][j]=display_poly(mod,Matrix[i][j])[0]
    return MatrixPretty,Matrix      
          

(add_table(2,[1,1,1]))  

###Asta merge pt field uri binare gen 2^oricat
'''   
    size=m.pow(mod,deg(f))
    Matrix = [[0 for x in range(size+1)] for y in range(size+1)] 
    MatrixOut = [[0 for x in range(size)] for y in range(size)] 
    MatrixPretty = [['0' for x in range(size)] for y in range(size)] 
    Matrix[0][0]='+'
    for i in range(1,size+1,1):
        Matrix[0][i]=bin(i-1)
        Matrix[i][0]=bin(i-1)   
    for i in range(1,size+1,1):
        for j in range(1,size+1,1):
            Matrix[i][j]=bin(int(Matrix[0][i],2)^int(Matrix[0][j],2))[2:].zfill(mod)       
    for i in range(0,size,1):
        for j in range(0,size,1):
            MatrixOut[i][j]=Matrix[i+1][j+1]
            MatrixOut[i][j]=[int(MatrixOut[i][j][k]) for k in range(mod)]
            MatrixOut[i][j]=elim_lead_zeros(MatrixOut[i][j])
            MatrixPretty[i][j]=display_poly(mod,MatrixOut[i][j])[0]
    return MatrixPretty,MatrixOut
'''