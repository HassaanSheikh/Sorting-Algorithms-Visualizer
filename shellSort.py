def shellSort(list):
    length = len(list)
    gap = length//2

    while gap > 0:
        for i in range(gap, length):
            anchor = list[i]
            x = i

            while x >= gap and list[x-gap] > anchor:
                list[x] = list[x-gap]
                x -= gap
            
            list[x] = anchor
        gap = gap//2