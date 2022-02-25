def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

seq = [5,6,7,3,2,13,7,4,1]
seq_sort = insertionSort(seq)
print(seq_sort) # [1, 2, 3, 4, 5, 6, 7, 7, 13]