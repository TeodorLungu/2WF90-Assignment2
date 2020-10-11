def reduction(number,mod):
    #Reduce modulo mod if necessary
        if number >= mod or number < 0:
            number = number - mod * (number//mod)
        return number   

def mul_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    mArray = [0 for i in range(lengthf+lengthg-1)]
    for i in range(lengthf):
        for j in range(lengthg):
            mArray[i+j]+=f[i]*g[j]
            mArray[i+j]=reduction(mArray[i+j],mod)
    return display_poly(mod,mArray)[0], mArray   

def display_poly(mod , poly):
    s = "" #The final result will be stored in string s
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹") #Make translation table to display superscripts
    k = len(poly) #Store the power for each term

    if poly == [0]:
        return "0", poly

    for i in range(len(poly)): #Iterate through the coefficients of the polynomial starting with the leading coefficient
        k = k - 1 #Subtract 1 from the current power. If this is the first subtraction then this will be the leading power of the polynomial
        #If the powers are 1 or 0 then the formatting of those terms doesn't need superscripts or even the X
        if (i != len(poly) - 1 and i != len(poly) - 2):
            term = "X" + str(k)
            term = term.translate(SUP)
        elif i == len(poly) - 2:
            term = "X"
        else:
            term = ""

        #Reduce modulo mod if necessary
        if poly[i] >= mod or poly[i] < 0:
            poly[i] = poly[i] - mod * (poly[i]//mod)
        
        #If the coefficient is 1 or 0 then it doesn't need to be shown
        if(poly[i] != 0 and (poly[i] != 1 or i == len(poly) - 1)):
            term = str(poly[i]) + term

        #The leading term does not need a + and if it is 0 then the following term doesn't need a plus either
        if (k != len(poly) - 1 and not (k == len(poly) - 2 and poly[0] == 0)):
                term = "+" + term
        
        #If the coefficient is 0 then the entire term doesn't need to be shown
        if (poly[i] != 0):
            s = s + term
    
    #Print and return the result
    return s, poly

def add_poly(mod,f,g):
    s = "" #The final result will be stored in string s
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)]
    if (lengthf == maximum):
        j=lengthf-1
        for i in range(lengthf):
            sArray[i]=f[i]
            reduction(sArray[i],mod)
        for i in range(lengthg-1,-1,-1):
            sArray[j]+=g[i]
            j=j-1
            reduction(sArray[i],mod)
    if (lengthg==maximum):
        j=lengthg-1
        for i in range(lengthg):
            sArray[i]=g[i]
            reduction(sArray[i],mod)
        for i in range(lengthf-1,-1,-1):
            sArray[j]+=f[i]
            j=j-1 
            reduction(sArray[i],mod)
    return display_poly(mod,sArray)[0], sArray
   
def sub_poly(mod,f,g):
    lengthf = len(f) #Store the power for each term
    lengthg = len(g)
    maximum = max(lengthf,lengthg)
    sArray = [0 for i in range(maximum)]
    if (lengthf == maximum):
        while (lengthg<maximum):
            g.insert(0,0)
            lengthg=len(g)
    if (lengthg == maximum):
        while (lengthf<maximum):
            f.insert(0,0)
            lengthf=len(f)        
    j=lengthf-1
    for i in range(lengthf):
        sArray[i]=f[i]
        reduction(sArray[i],mod)
    for i in range(lengthg-1,-1,-1):
        sArray[j]-=g[i]
        j=j-1
        reduction(sArray[i],mod)
    return display_poly(mod,sArray)[0], sArray    

def lc(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return p[i]
    return 0

def deg(p):
    for i in range(len(p)):
        if(p[i] != 0):
            return len(p)-i-1
    return 0

def mod_inverse(mod, a):
    aPrime = a
    mPrime = mod
    x_1 = 1
    x_2 = 0
    while mPrime > 0:
        q = int(aPrime/mPrime)
        r = aPrime - q*mPrime
        aPrime = mPrime
        mPrime = r
        x_3 = x_1 - q*x_2
        x_1 = x_2
        x_2 = x_3
    if aPrime == 1:
        return x_1
    else:
        return 0

def elim_lead_zeros(p):
    d = deg(p)
    pPrime = [0 for i in range(d+1)]
    k = 0
    for i in range(len(p)-d-1,len(p)):
        pPrime[k] = p[i]
        k = k + 1
    return pPrime
        
def long_div_poly(mod,a,b):
    if deg(b) == 0: #Division with a scalar
        digit = b[-1]
        digit = mod_inverse(mod,digit)
        result = mul_poly(mod,a,[digit])[1]
        r = [0]
        return display_poly(mod,result)[0],display_poly(mod,r)[0],result,r
    maximum = max(len(a),len(b))
    q = [0 for i in range(maximum)]
    r = a
    while deg(r)>=deg(b):
        x = [0 for i in range(maximum)]
        inv = mod_inverse(mod, lc(b))
        q_i = reduction(inv*lc(r),mod)
        d = deg(r) - deg(b)
        x[-(d+1)] = q_i
        q = add_poly(mod, q, x)[1]
        r = sub_poly(mod,r,mul_poly(mod,x,b)[1])[1]
        q = display_poly(mod,q)[1]
        r = display_poly(mod,r)[1]
    q = elim_lead_zeros(q)
    r = elim_lead_zeros(r)
    return display_poly(mod,q)[0],display_poly(mod,r)[0],q,r
