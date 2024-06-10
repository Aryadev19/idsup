from probability import normal_pdf,normal_cdf,inverse_normal_cdf
import math
import random
def normal_approximation_to_binomial(n, p):
   mu = p * n
   sigma = math.sqrt(p * (1 - p) * n)
   return mu, sigma

# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf
# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
   return 1 - normal_cdf(lo, mu, sigma)
# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
   return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)
# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
   return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
   return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
   return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
   tail_probability = (1 - probability) / 2
   # upper bound should have tail_probability above it
   upper_bound = normal_lower_bound(tail_probability, mu, sigma)
   # lower bound should have tail_probability below it
   lower_bound = normal_upper_bound(tail_probability, mu, sigma)
   return lower_bound, upper_bound

def two_sided_p_value(x, mu=0, sigma=1):
   if x >= mu:
   # if x is greater than the mean, the tail is what's greater than x
      return 2 * normal_probability_above(x, mu, sigma)
   else:
   # if x is less than the mean, the tail is what's less than x
      return 2 * normal_probability_below(x, mu, sigma)

def run_experiment():
   return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
   num_heads = len([flip for flip in experiment if flip])
   return num_heads < 469 or num_heads > 531

def estimated_parameters(N, n):
   p = n / N
   sigma = math.sqrt(p * (1 - p) / N)
   return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
   p_A, sigma_A = estimated_parameters(N_A, n_A)
   p_B, sigma_B = estimated_parameters(N_B, n_B)
   return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

def B(alpha, beta):
   return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
   if x < 0 or x > 1: # no weight outside of [0, 1]
      return 0
   return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
