def insertionsort(sortable):
    for each in range (1,len(sortable)):
        #print (each)
        key = sortable[each]
        #print (key)
        i = (each - 1)
        #print (i)
        #print (sortable[i])
        while i >= 0 and int(sortable[i]) > int(key):
            #print ("%d iteration" %each)
            #print (i)
            #print (each)
            sortable[i+1] = sortable[i]
            sortable [i] = key 
            i = (i - 1)
            #print (sortable)
    return sortable

sortable = [ x for x in range(5000,1,-1)]

import time
start_time = time.time()

print (insertionsort(sortable))

print("Process finished --- %s seconds ---" % (time.time() - start_time))
