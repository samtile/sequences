import itertools as it

# Sam's first gap sequence - to be added to the OEIS
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
    requiredTerms = 100
    sequence = [None] * (requiredTerms*2)
    k,v = 0,1
    max = 0
    while True:
        sequence[k] = v
        if (v > max):
            max = v
        u = sequence.index(None)
        if u >= requiredTerms:
            break
        elif u < k:
            # advance backward, and decrement v by that much too
            d = k - u
            (k, v) = (k - d, v - d)
        else:
            # skip forward v, then advance to the next unfilled position
            (k, v) = (sequence.index(None, k + v), max + 1)
    for result in range(requiredTerms):
        print(sequence[result])

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

# Aaron's newest, based on sequence one with a slight change to add both adjacent terms on the backward steps
def sequenceFive():
    requiredTerms = 5000
    sequence = [None] * (requiredTerms*5)
    sequence[0] = 1
    maxValue = 1
    lastValue = 1
    firstUnpopulatedN = 1
    n = 0
    while 1:
        if firstUnpopulatedN >= requiredTerms:
            break
        if firstUnpopulatedN < n:
            sequence[firstUnpopulatedN] = lastValue - n + firstUnpopulatedN + sequence[firstUnpopulatedN-1]
            if(sequence[firstUnpopulatedN+1]!=None):
                sequence[firstUnpopulatedN] = sequence[firstUnpopulatedN] + sequence[firstUnpopulatedN+1]
            n = firstUnpopulatedN
            lastValue = sequence[n]
            firstUnpopulatedN += 1
            while sequence[firstUnpopulatedN] != None:
                firstUnpopulatedN += 1
        else:
            n = n + lastValue
            while 1:
                if sequence[n] != None:
                    n += 1
                else:
                    break
            sequence[n] = next(i for i in range(maxValue,requiredTerms*10) if i not in sequence and i!=0)
            lastValue = sequence[n]
            if n == firstUnpopulatedN:
                firstUnpopulatedN += 1
                while sequence[firstUnpopulatedN] != None:
                    firstUnpopulatedN += 1
    for result in range(requiredTerms):
        print(sequence[result])

#sequenceZero()
#sequenceOne()
#sequenceTwo()
#sequenceThree()
#sequenceFour()
sequenceFive()