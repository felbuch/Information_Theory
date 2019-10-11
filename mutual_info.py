def mutual_info(array_of_joint_probabilities):
    '''Muutal information of X and Y.
        The array of probabilities contains the joint distribution of (X,Y).
        We make use of the property I(X,Y) = H(X) + H(Y) - H(X,Y)'''
    X = list(array_of_joint_probabilities.sum(axis = 0))
    Y = list(array_of_joint_probabilities.sum(axis = 1))
    return(entropy(X) + entropy(Y) - joint_entropy(array_of_joint_probabilities))
