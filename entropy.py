def entropy(list_of_probabilities):
    """Entropy.
    This function is defined as a special case of the cross entropy when both probability lists are equal"""
    return(crossentropy(list_of_probabilities, list_of_probabilities))
