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

