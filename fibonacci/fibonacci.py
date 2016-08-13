fibonacci = []
limitNumber = int(input("Ingrese el número limite para la serie: "))
base = 0
lastValue = 1
while True:
    print("lastValue " + str(lastValue))
    newLasValue = base + lastValue
    if newLasValue >= limitNumber:
        break
    else:
        base = lastValue
        lastValue = newLasValue
        fibonacci.append(lastValue)

print(fibonacci)
