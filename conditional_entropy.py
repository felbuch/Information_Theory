def conditional_entropy(array_of_joint_probabilities, condition_var = 0):
    '''Conditional probability.
    The array_of_joint_probabilities contains the joint distribution of (X,Y).
    condition_var will be 0 or 1 depending on whether the Y variable in H(X|Y) is in the row (1) or in the column (0)
    We make use of the property H(X|Y) = H(X,Y) - H(Y)'''
    
    list_of_prob_of_condition = list(array_of_joint_probabilities.sum(axis = condition_var))    
    return(joint_entropy(array_of_joint_probabilities) - entropy(list_of_prob_of_condition))
