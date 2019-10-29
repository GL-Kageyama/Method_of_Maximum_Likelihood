#=====================================================================
#--------------       Method of Maximum Likelihood       -------------
#=====================================================================
# Method of estimating the parameters of a probability 
# distribution by maximizing a likelihood function.
#=====================================================================
# Pattern 1 : Basic implementation 
#=====================================================================

def calc_factorial(n):
	res = 1
	for i in range(0, n):
		idx = i + 1
		res = res*idx
	return res

def calc_bin_coef(n, k):
	res = calc_factorial(n) / (calc_factorial(k)*calc_factorial(n - k))
	return res

def calc_binom_pmf(n, k, p):
	res = calc_bin_coef(n, k)*(p**k)*(1 - p)**(n - k)
	return res

print("")

print(calc_binom_pmf(1000, 500, 0.6))
print(calc_binom_pmf(1000, 550, 0.6))
print(calc_binom_pmf(1000, 575, 0.6))
print(calc_binom_pmf(1000, 590, 0.6))
print(calc_binom_pmf(1000, 595, 0.6))
print(calc_binom_pmf(1000, 598, 0.6))
print(calc_binom_pmf(1000, 599, 0.6))

# Maximum value is obtained at 600.
print("----------------------------------")
print(calc_binom_pmf(1000, 600, 0.6))
print("----------------------------------")

print(calc_binom_pmf(1000, 601, 0.6))
print(calc_binom_pmf(1000, 602, 0.6))
print(calc_binom_pmf(1000, 605, 0.6))
print(calc_binom_pmf(1000, 610, 0.6))
print(calc_binom_pmf(1000, 625, 0.6))
print(calc_binom_pmf(1000, 650, 0.6))
print(calc_binom_pmf(1000, 700, 0.6))

print("")
print("===========================================")
print("")

#=====================================================================
# Pattern 2 :  Using Scipy's API
#=====================================================================

from scipy.stats import binom

print(binom.pmf(500, 1000, 0.6))
print(binom.pmf(550, 1000, 0.6))
print(binom.pmf(575, 1000, 0.6))
print(binom.pmf(590, 1000, 0.6))
print(binom.pmf(595, 1000, 0.6))
print(binom.pmf(598, 1000, 0.6))
print(binom.pmf(599, 1000, 0.6))

# Maximum value is obtained at 600.
print("----------------------------------")
print(binom.pmf(600, 1000, 0.6))
print("----------------------------------")

print(binom.pmf(601, 1000, 0.6))
print(binom.pmf(602, 1000, 0.6))
print(binom.pmf(605, 1000, 0.6))
print(binom.pmf(610, 1000, 0.6))
print(binom.pmf(625, 1000, 0.6))
print(binom.pmf(650, 1000, 0.6))
print(binom.pmf(700, 1000, 0.6))

print("")

