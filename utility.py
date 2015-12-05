import math

def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)
def epsilon_not_equal(n, m, epsilon=0.00001):
   return (n - epsilon) > m or (n + epsilon < m)