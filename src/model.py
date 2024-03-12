
def add(x:float, y:float) -> float: 
    """
        arguments: 
            x(float) : argument  
            y(float) : argument 
        
            return : 
                resultat(float)
    """
    return x + y

def sub(x:float, y:float) -> float: 
    """
        arguments: 
            x(float) : argument  
            y(float) : argument 
        
            return : 
                resultat(float)
    """
    return x - y

def mult(x:float, y:float) -> float: 
    """
        arguments: 
            x(float) : argument  
            y(float) : argument 
        
            return : 
                resultat(float)
    """
    return x * y

def div(x:float, y:float) -> float: 
    """
        arguments: 
            x(float) : argument  
            y(float) : argument  non nul 
        
            return : 
                resultat(float)
    """
    if y==0: 
        raise ZeroDivisionError("On ne divise pas par zero")
    
    return x / y

