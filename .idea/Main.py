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