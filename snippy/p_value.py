import scipy.stats

def p_value(chisq, ndof):
    p = scipy.stats.chi2.cdf(chisq, ndof)
    # If the probability is > 50% , take the complement.
    if p > 0.5:
        p = 1.0 - p
    return p

print(p_value(10.0, 10))
print(p_value(9.34181776559197, 10))
print(p_value(3.9402991361190605, 10))
print(p_value(18.307038053275146, 10))
