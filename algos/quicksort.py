import sys
sys.setrecursionlimit(100000)
def quicksort(A,l,r):
    if (r-l) <= 1:
        return ()
    yellow = l+1
    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[yellow],A[green]) = (A[green],A[yellow])
            yellow = yellow + 1
    (A[l],A[yellow-1]) = (A[yellow-1],A[l])

    quicksort(A, l, yellow-1)
    quicksort(A, yellow, r)
    return (A)


unsortedarray = [x for x in range(100,1,-1)]
print (unsortedarray)
print (quicksort(unsortedarray, 0,len(unsortedarray)))


