def isPrime(p):
    if p > 1:
        for i in range(2, p//2):
            if (p % i) == 0:
                return False
        return True        
    else:
        return False

def reduction(number,mod):
    #Reduce modulo mod if necessary
        if number >= mod or number < 0:
            number = number - mod * (number//mod)
        return number    
