###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1

def generate_eggs(egg_weights, n):
    for i in range(n):
        for w in egg_weights:
            yield w

def helper(egg_weights, target_weight, solution, memo):
    if target_weight == 0:
        return len(solution)

    if target_weight < 0 or len(egg_weights) == 0:
        return None

    k = str((len(solution), target_weight)) 
    if k in memo.keys():
        return memo[k]


    w = egg_weights[0]
    egg_weights = egg_weights[1:]

    s1 = helper(egg_weights, target_weight - w, solution + [w], memo)
    s2 = helper(egg_weights, target_weight, solution, memo)

    if s1 is not None and s2 is not None:
        if s1 < s2: 
            memo[k] = s1
            return s1
        else: 
            memo[k] = s2
            return s2

    if s1 is not None: 
        memo[k] = s1
        return s1

    if s2 is not None: 
        memo[k] = s2
        return s2

    return None


def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """

    eggs_values = [g for g in generate_eggs(egg_weights, target_weight)]
    
    r= helper(eggs_values, target_weight, [], memo)

    return r 

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
