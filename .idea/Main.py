# Sam's second gap sequence - to be added to the OEIS
def sequenceOne():
    iterations = 10000
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
                sequence[y] = lastNumber - lastN + y
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

# Aaron's first gap sequence
def sequenceTwo():
    iterations = 60000
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

# Luca's first gap sequence - to be added to the OEIS
def sequenceThree():
    iterations = 1000
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

#sequenceOne()
#sequenceTwo()
sequenceThree()