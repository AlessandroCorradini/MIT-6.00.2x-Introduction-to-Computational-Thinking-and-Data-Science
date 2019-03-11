## Exercise 2

1. You are given the following partially completed function and a file julytemps.txt containing the daily maximum and minimum temperatures for each day in Boston for the 31 days of July 2012. In the loop, we need to make sure we ignore all lines that don't contain the relevant data.

```
def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        # FILL THIS IN
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)
```

Be sure that you have looked through the raw data file and that you understand which lines do and do not contain relevant data. Which set of conditions would capture all non-data lines (ie, provide a filter that would catch anything that wasn't relevant data)? fields is the variable that contains a list of elements in a line.


- ```if len(fields) != 3:```
- ```if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:```
- ```if not fields[0].isdigit() or len(fields) < 3:```
- ```if len(fields) < 3 or not fields[0].isdigit(): ``` [X]
- ```if '-' == fields[0] or 'Boston' == fields[0] or 'Day' == fields[0] or ' ' == fields[0]:```
- ```if '-' == fields[0] or 'Boston' == fields[0] or 'Day' == fields[0]:```

2. Suppose you defined ```diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))``` to be a list which is the element-by-element difference between ```highTemps``` and ```lowTemps```. Which is a valid plotting statement for a graph with days on the horizontal axis and the temperature difference on the vertical axis?


- ```pylab.plot(highTemps,lowTemps)```
- ```pylab.plot(range(1,32), highTemps)```
- ```pylab.plot(range(1,32), lowTemps)```
- ```pylab.plot(range(1,32), diffTemps)``` [X]
- ```pylab.plot(diffTemps, range(1,32))```