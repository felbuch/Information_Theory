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

