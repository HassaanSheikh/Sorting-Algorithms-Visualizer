def bubbleSort(list):
    length = len(list)

    for x in range(length-1):
        sorted = False

        for i in range(length-1-x):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                sorted = True
        if sorted == False:
            break