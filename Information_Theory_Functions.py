import numpy as np


def log2(x):
    """Logarithm of x in base 2."""
    
    assert x > 0, "x must be positive"
    
    log = np.log(x)/np.log(2)
    
    return(log)



def information_of_event(p):
    """Information content of an event, in bits"""

    assert p >= 0, "probabilities cannot be negative"

    if p > 0:
        return -1 * log2(p)
    else:
        #Information of an impossible event is zero, by definition.
        #What cannot happen, cannot surprise us.
        #This will be important to avoid errors when calculating p*log(1/p) terms in entropy.
        return 0



def assert_validity_of_probability_distribution(list_of_probabilities):
    '''An auxiliary function. Verifies that a probability distribution satisfies basic requirements of being positive, less than unity and sums up to 1.'''
    assert all(p >= 0 for p in list_of_probabilities), "All probabilities must be non-negative"
    assert all(p <= 1 for p in list_of_probabilities), "Probabilities cannot be greater than 1"
    assert round(sum(list_of_probabilities),10) == 1, "Probabilities should add 1"
    return 0



def crossentropy(list_of_true_probabilities,list_of_believed_probabilities):
    """Cross entropy of a probability distribution. 
    The distributions are given as lists of probabilities, one named "true" and one named "believed".
    The true distribution appears in the calculation of the expected value, 
    whereas the believed distribution appears in the calculation of the surprise.
    This is the main function we define.
    All subsequent functions will be defined in terms of this one"""

    #Test if lists of probabilities are valid
    #Test if first list is valid
    assert len(list_of_true_probabilities) == len(list_of_believed_probabilities), "Both lists of probabilities should have the same length"
    assert_validity_of_probability_distribution(list_of_true_probabilities)
    #If lists are different, test if second list is also valid
    if list_of_true_probabilities != list_of_believed_probabilities:
        assert_validity_of_probability_distribution(list_of_believed_probabilities)
    else:
        pass
    
    #Calculates cross-entropy
    entropy = 0.0
    for p, q in zip(list_of_believed_probabilities, list_of_true_probabilities):
        if q > 0:
            entropy += q * information_of_event(p)
        elif q == 0:
            #If p = 0, we make 0 * log(1/0) = 0.
            #We can show this makes sense using L'Hopital's theorem,
            #but we will not discuss it here.
            entropy += 0
        else:
            raise ValueError("Unknown error. Sorry.")
    return entropy 




def entropy(list_of_probabilities):
    """Entropy.
    This function is defined as a special case of the cross entropy when both probability lists are equal"""
    return(crossentropy(list_of_probabilities, list_of_probabilities))




def KL(list_of_probabilities_1, list_of_probabilities_2):
    '''Kullback-Leibler divergence, D(P||Q).
    The probability distribution P is represented by the list_of_probabilities_1.
    The probability distribution Q is represented by the list_of_probabilities_2.
    We use the formula KL = H(p,q) - H(p)'''
    divergence = crossentropy(list_of_probabilities_1, list_of_probabilities_2) - entropy(list_of_probabilities_1)
    return(divergence)




def joint_entropy(array_of_joint_probabilities):
    '''Joint probability.
    array_of_joint_probabilities is a 2 dimensional numpy array which
    brings contains the joint probabilities of two random variables, X and Y'''
    entropy = 0
    for line in array_of_joint_probabilities:
        for p in line:
            entropy += p * information_of_event(p)
    return(entropy)




def conditional_entropy(array_of_joint_probabilities, condition_var = 0):
    '''Conditional probability.
    The array_of_joint_probabilities contains the joint distribution of (X,Y).
    condition_var will be 0 or 1 depending on whether the Y variable in H(X|Y) is in the row (1) or in the column (0)
    We make use of the property H(X|Y) = H(X,Y) - H(Y)'''
    
    list_of_prob_of_condition = list(array_of_joint_probabilities.sum(axis = condition_var))    
    return(joint_entropy(array_of_joint_probabilities) - entropy(list_of_prob_of_condition))
    



def mutual_info(array_of_joint_probabilities):
    '''Muutal information of X.
        The array of probabilities contains the joint distribution of (X,Y).
        We make use of the property I(X,Y) = H(X) + H(Y) - H(X,Y)'''
    X = list(array_of_joint_probabilities.sum(axis = 0))
    Y = list(array_of_joint_probabilities.sum(axis = 1))
    return(entropy(X) + entropy(Y) - joint_entropy(array_of_joint_probabilities))
    



