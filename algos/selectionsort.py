def selectionsort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i] < l[start]:
                minpos = i
        (l[start],l[minpos]) = (l[minpos],l[start])
    return l


x = [3,9,6,1,9,0]
print (selectionsort(x))