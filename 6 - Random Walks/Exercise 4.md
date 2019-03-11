## Exercise 4

Suppose we wanted to create a class PolarBearDrunk, a drunk polar bear who moves randomly along the x and y axes taking large steps when moving South, and small steps when moving North.
```
class PolarBearDrunk(Drunk):
    def takeStep(self):
        # code for takeStep()
```
Which of the following would be an appropriate implementation of takeStep()?

Option A)

```
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]
myDirection = random.choice(directionList)
if myDirection[0] == 0.0:
    return myDirection + (0.0, -0.5)
return myDirection
```

Option B)

```
directionList = [(0.0, 0.5), (1.0, -0.5), (-1.0, -0.5), (0.0, -1.5)]
return random.choice(directionList)
```

Option C)

```
directionList = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.5)]
return random.choice(directionList)
```

Option D)

```
directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, -1.0)]
return random.choice(directionList)
```

- Option A)
- Option B)
- Option C) [X]
- Option D)
