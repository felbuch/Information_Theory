def KL(list_of_probabilities_1, list_of_probabilities_2):
    '''Kullback-Leibler divergence, D(P||Q).
    The probability distribution P is represented by the list_of_probabilities_1.
    The probability distribution Q is represented by the list_of_probabilities_2.
    We use the formula KL = H(p,q) - H(p)'''
    divergence = crossentropy(list_of_probabilities_1, list_of_probabilities_2) - entropy(list_of_probabilities_1)
    return(divergence)
