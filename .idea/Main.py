# Sam's firs gap sequence - to be added to the OEIS
def sequenceZero():
    iterations = 20000
    sequence = [0] * (iterations*2)
    sequence[0] = 1
    maxNumber = 1
    lastNumber = 1
    lastN = 0
    done = 0
    for x in range(iterations):
        done = 0
        for y in range(lastN):
            if sequence[y] == 0:
                sequence[y] = lastNumber + 1
                maxNumber = sequence[y]
                lastNumber = sequence[y]
                lastN = y
                done = 1
                break
        if done == 0:
            lastN = lastN + lastNumber
            while 1:
                if sequence[lastN] != 0:
                    lastN = lastN + 1
                else:
                    break
            sequence[lastN] = maxNumber + 1
            lastNumber = maxNumber + 1
            maxNumber = maxNumber + 1
    for results in range(iterations):
        print(sequence[results])

# Sam's second gap sequence - to be added to the OEIS
def sequenceOne():
    iterations = 2000
    sequence = [0] * (iterations*2)
    sequence[0] = 1
    maxValue = 1
    lastValue = 1
    n = 0
    done = 0
    for x in range(iterations):
        done = 0
        for y in range(n):
            if sequence[y] == 0:
                sequence[y] = lastValue - n + y
                lastValue = sequence[y]
                n = y
                done = 1
                break
        if done == 0:
            n = n + lastValue
            while 1:
                if sequence[n] != 0:
                    n = n + 1
                else:
                    break
            sequence[n] = maxValue + 1
            lastValue = maxValue + 1
            maxValue = maxValue + 1
    for results in range(iterations):
        print(sequence[results])

# Aaron's first gap sequence
def sequenceTwo():
    iterations = 1000
    sequence = [0] * (iterations*2)
    processed = [0] * (iterations*2)
    sequence[0] = 1
    for x in range(iterations):
        count = 0
        while(1):
            if processed[count] == 1 or sequence[count] == 0:
                count = count + 1
            else:
                break
        if count - sequence[count] >= 0:
            if sequence[count - sequence[count]] == 0:
                sequence[count - sequence[count]] = sequence[count] + 1
        if sequence[count + sequence[count]] == 0:
            sequence[count + sequence[count]] = sequence[count] + 1
        processed[count] = 1
    for results in range(iterations):
        print(sequence[results])

# We thought this was Luca's first gap sequence - but I had misunderstood it and chad created a brand new sequence! - to be added to the OEIS
def sequenceThree():
    iterations = 430000
    sequence = [0] * (iterations*2)
    sequence[0] = 1
    lastNumber = 1
    lastN = 0
    done = 0
    for x in range(iterations):
        done = 0
        for y in range(lastN):
            if sequence[y] == 0:
                sequence[y] = sequence[y-1] + sequence[y+1]
                lastNumber = sequence[y]
                lastN = y
                done = 1
                break
        if done == 0:
            lastN = lastN + lastN + lastNumber + 1
            while 1:
                if sequence[lastN] != 0:
                    lastN = lastN + 1
                else:
                    break
            sequence[lastN] = lastNumber + 1
            lastNumber = lastNumber + 1
    for results in range(iterations):
        print(sequence[results])

# Luca's gap sequence
def sequenceFour():
    iterations = 20000
    sequence = [0] * (iterations*2)
    sequence[0] = 1
    lastNumber = 1
    lastN = 0
    maxN = 0
    done = 0
    for x in range(iterations):
        done = 0
        for y in range(lastN):
            if sequence[y] == 0:
                sequence[y] = sequence[y-1] + sequence[y+1]
                lastNumber = sequence[y]
                lastN = y
                done = 1
                break
        if done == 0:
            lastN = lastN + lastN + lastNumber + 1
            while 1:
                if sequence[lastN] != 0:
                    lastN = lastN + 1
                else:
                    break
            sequence[lastN] = sequence[maxN] + 1
            lastNumber = lastNumber + 1
            if lastN > maxN:
                maxN = lastN
    for results in range(iterations):
        print(sequence[results])

#sequenceZero()
sequenceOne()
#sequenceTwo()
#sequenceThree()
#sequenceFour()