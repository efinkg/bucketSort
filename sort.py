__author__ = 'glassman'
from generateArray import *
import math

def makebuckets(n):
    array = getArray(n)
    buckets = []
    i = 0
    while(i<n):
        buckets.append([])
        i+=1
    fillbuckets(array,buckets)

def fillbuckets(array, buckets):
    largest = max(array)
    for point in array:
        bucketnum = (int(math.ceil((point/largest)*len(buckets))))
        #print str(point) + " goes in " + str(bucketnum)
        buckets[bucketnum-1].append(point)
    print(buckets)
    sort(buckets)

def sort(buckets):
    for bucket in buckets:
        i = 1
        while (i < len(bucket)):
            compare = bucket[i]
            j = i
            while j > 0 and bucket[j-1] > compare:
                #print(bucket[j-1])
                #print(compare)
                bucket[j] = bucket[j-1]
                j = j-1
            bucket[j] = compare
            i+=1
        #print(bucket)
    combine(buckets)

def combine(buckets):
    sortedarray = []
    for bucket in buckets:
        for item in bucket:
            sortedarray.append(item)
    print sortedarray
    verify(sortedarray)

def verify(sortedarray):
    min = sortedarray[0]
    for item in sortedarray:
        if item < min:
            print "Failed " + str(item) + " is less than " + str(min)
        min = item

def main():
    n = 5
    makebuckets(n)

if __name__ == "__main__":
    main()