def bubble_sort(table):
    result = table
    if not result:
        return result
    temp = 0
    for i in range(0, len(table)-1):
        for j in range(0, len(table)-i-1):
            if result[j] > result[j+1]:
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp
    return result


ciag = []
ciag.append([])
ciag.append([1,2])
ciag.append([1,2,5,3,1,7,9,1,12,83,1,5,3,2])
ciag.append([1,1,1,1,1,1,1,2,1,1,1])
ciag.append([2,2,2,2])
ciag.append([1,2])
ciag.append([2,1])

for i in range(0, len(ciag)):
    print('Before sorting: ', ciag[i])
    print('After sorting : ', bubble_sort(ciag[i]))



