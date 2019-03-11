Exercise 1

1. Would placing the drunk's starting location not at the origin change the distances returned?

- Yes
- No [X]

If so, what line would you modify to compensate? Enter the line number (eg 17). If not, just type None.

```
def simWalks(numSteps, numTrials, dClass):
     homer = UsualDrunk()
     notOrigin = Location(1, 0)
     distances = []
     for t in range(numTrials):
         f = Field()
         f.addDrunk(homer, notOrigin)
         distances.append(round(walk(f, homer, numSteps), 1))
    return distances
```

None

2. If you were going to use random.seed in a real-life simulation instead of just when you are debugging a simulation, would you want to seed it with 0?

- Yes
- No [X]