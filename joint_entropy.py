def joint_entropy(array_of_joint_probabilities):
    '''Joint probability.
    array_of_joint_probabilities is a 2 dimensional numpy array which
    brings contains the joint probabilities of two random variables, X and Y'''
    entropy = 0
    for line in array_of_joint_probabilities:
        for p in line:
            entropy += p * information_of_event(p)
    return(entropy)
