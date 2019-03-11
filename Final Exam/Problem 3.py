# You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. 
# Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

# Write a Monte Carlo simulation that meets the specifications below. Feel free to write a 
# helper function if you wish.

# def drawing_without_replacement_sim(numTrials):
#     '''
#     Runs numTrials trials of a Monte Carlo simulation
#     of drawing 3 balls out of a bucket containing
#     4 red and 4 green balls. Balls are not replaced once
#     drawn. Returns a float - the fraction of times 3 
#     balls of the same color were drawn in the first 3 draws.
#     '''
#     # Your code here 
# Paste your entire function (including the definition) in the box.

# Restrictions:

# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    counter = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        picks = []
        for j in range(3):
            k = random.choice(bucket)
            picks.append(k)
            bucket.remove(k)
        if picks[0] == picks[1] == picks[2]:
            counter += 1
    return counter/numTrials