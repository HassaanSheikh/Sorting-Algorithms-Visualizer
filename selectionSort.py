def selectionSort(list):
    length = len(list)
    for i in range(length-1):
        minIndex = i

        for x in range(minIndex+1, length):
            if list[x] < list[minIndex]:
                minIndex = x
        if i != minIndex:
            list[i], list[minIndex] = list[minIndex], list[i]