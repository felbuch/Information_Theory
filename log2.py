import numpy as np


def log2(x):
    """Logarithm of x in base 2."""
    
    assert x > 0, "x must be positive"
    
    log = np.log(x)/np.log(2)
    
    return(log)
