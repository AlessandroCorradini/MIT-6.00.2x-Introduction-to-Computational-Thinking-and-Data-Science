## Exercise 2

1. Is the following code deterministic or stochastic?

```
import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)
```

- Deterministic
- Stochastic [X]

2. Which of the following alterations (Code Sample A or Code Sample B) would result in a deterministic process?

```
import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)

    
    
# Code Sample B
mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print(mylist)

Check one, none, or both.
```

- Code Sample A [X]
- Code Sample B [X]
