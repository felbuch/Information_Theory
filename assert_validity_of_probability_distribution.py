def assert_validity_of_probability_distribution(list_of_probabilities):
    '''An auxiliary function. Verifies that a probability distribution satisfies basic requirements of being positive, less than unity and sums up to 1.'''
    assert all(p >= 0 for p in list_of_probabilities), "All probabilities must be non-negative"
    assert all(p <= 1 for p in list_of_probabilities), "Probabilities cannot be greater than 1"
    assert round(sum(list_of_probabilities),10) == 1, "Probabilities should add 1"
    return 0

