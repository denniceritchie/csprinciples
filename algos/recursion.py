def length(l):
    print (l)
    if l == []:
       return(0)
    else:
        return(1+length(l[1:]))

l = [1,4,5,6,8,0]
print (length(l))


