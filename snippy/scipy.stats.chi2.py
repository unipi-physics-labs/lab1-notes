import scipy.stats

dof = 12
value = 5.0
chi2 = scipy.stats.chi2(dof)
p_value = chi2.cdf(value)
print(p_value)
print(chi2.ppf(p_value))
