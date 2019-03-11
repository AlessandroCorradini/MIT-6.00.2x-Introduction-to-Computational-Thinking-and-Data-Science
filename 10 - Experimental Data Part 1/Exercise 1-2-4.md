## Exercise 1

Using the formula derived in this segment, compute k from the second experimental observation: m = 0.15 kg, x = 0.1015 m.

Use 9.81 m/s^2 as the gravitational constant (g). Enter your answer to at least 1 decimal place of accuracy.

k = 14.497

## Exercise 2
2/2 points (graded)
Which of the following lines will fit a parabola to the spring data given in the lecture file, springData.txt? Check all that work.

- ```a,b = pylab.polyfit(xVals, yVals, 2)```
- ```model = pylab.polyfit(xVals, yVals, 2)``` [X]
- ```a,b,c = pylab.polyfit(xVals, yVals, 2)``` [X]

Suppose the coefficients returned by polyval are in the tuple (c1, c2, c3). Which of the following lines calculate the estimated y values?

- ```estYVals = c1*xVals**2 + c2*xVals + c3``` [X]
- ```estYVals = c3*xVals**2 + c2*xVals + c1```

Exercise 4

Recall from the previous video the concept of the coefficient of determination, also known as the  value. This is computed by 

1 - ((variability errors)^2/(variability data)^2). 

The variability of the errors is computed by taking the sum of the squares of (observed - predicted) errors. We normalize this variablity by dividing it by the variability of the data, which is sum of the squares of (observation - average_observation) for each observation.

In this file, this R^2 value is computed by the function rSquare.

In that file, revise fitData and fitData3 to report the coefficient of determination for the fitted line in each case. Did this measure of the "goodness of fit" improve when we eliminated the measurements after the spring reached its elastic limit and Hooke's Law no longer applied?

- Yes [X]
- No