def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i+j < m+n :
        if i==m:
            C.append(B[j])
            j = j+1
        elif j==n:
            C.append(A[i])
            i = i+1
        elif A[i] < B[j]:
            C.append(A[i])
            i = i+1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j +1
        elif A[i] == B[j]:
            C.append(A[i])
            i = i+1
            j = j+1
    return C

#x = [6,7,10,33,55]
#y = [91,100,109,560,788,3900,1065]
#print (x)
#print (y)
#print (merge(x,y))
def mergesort(A,left,right):
    if right - left <= 1:
        return (A[left:right])
    if right - left > 1:
        mid = (right + left) // 2
        L = mergesort(A, left,mid)
        R = mergesort(A, mid, right)
        return (merge(L, R))
x = [x for x in range (1,1000000,2)]
y = [ y for y in range (0,1000000,2)]

A = x + y
print (mergesort(A, 0,len(A)))


    