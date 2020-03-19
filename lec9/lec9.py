# Lecture 9
#----------------------------------#
# Binary Search 
def bsearch(s, e, first, last, calls):
    print(first, last, calls)
    if (last - first) < 2:
        return s[first] == e or s[last] == e
    mid = first + (last - first)//2 # // - return integer after divide
    if s[mid] == e :
        return True
    if s[mid] > e:
        return bsearch(s, e, first, mid-1, calls+1)
    return bsearch(s, e, mid +1, last, calls + 1)

def search(s, e):
 print(bsearch(s, e, 0, len(s) - 1, 1)) 

# Output for Binary Search 
# Suppose we have to find 1 in 1000000
"""
>>> s = range(1000000)
>>> le.search(s, 1)
0 999999 1
0 499998 2
0 249998 3
0 124998 4
0 62498 5
0 31248 6
0 15623 7
0 7810 8
0 3904 9
0 1951 10
0 974 11
0 486 12
0 242 13
0 120 14
0 59 15
0 28 16
0 13 17
0 5 18
0 1 19
True
>>>
"""
#----------------------------------------#
# Selection sort

def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j = j + 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp

def testSelSort():
    test1 = [1,6,3,4,5,2]
    input('run selective test 1')
    selSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run selective test 2')
    selSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run selective test 3')
    selSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run selective test 4')
    selSort(test4) 
# Output for Selection Sort is 
"""
Type "help", "copyright", "credits" or "license" for more information.
>>> import lec9 as le
>>> le.testSelSort()
run selective test 1
[1, 6, 3, 4, 5, 2]
[1, 6, 3, 4, 5, 2]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
run selective test 2
[6, 1, 2, 3, 4, 5]
[1, 6, 2, 3, 4, 5]
[1, 2, 6, 3, 4, 5]
[1, 2, 3, 6, 4, 5]
[1, 2, 3, 4, 6, 5]
run selective test 3
[6, 5, 4, 3, 2, 1]
[1, 5, 4, 3, 2, 6]
[1, 2, 4, 3, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
run selective test 4
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
"""


#----------------------------------------#
# Bubble Sort

def bubbleSort(L):
    for j in range(len(L)):
        print(L)
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp


def  testBubbleSort():
    test1 = [1,6,3,4,5,2]
    input('run bubble test 1')
    bubbleSort(test1)
    test2 = [6,1,2,3,4,5]
    input('run bubble test 2')
    bubbleSort(test2)
    test3 = [6,5,4,3,2,1]
    input('run bubble test 3')
    bubbleSort(test3)
    test4 = [1,2,3,4,5,6]
    input('run bubble test 4')
    bubbleSort(test4) 


# Output for Buuble sort is 
"""
Type "help", "copyright", "credits" or "license" for more information.
>>> import lec9 as le
>>> le.testBubbleSort()
run bubble test 1
[1, 6, 3, 4, 5, 2]
[1, 3, 4, 5, 2, 6]
[1, 3, 4, 2, 5, 6]
[1, 3, 2, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
run bubble test 2
[6, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
run bubble test 3
[6, 5, 4, 3, 2, 1]
[5, 4, 3, 2, 1, 6]
[4, 3, 2, 1, 5, 6]
[3, 2, 1, 4, 5, 6]
[2, 1, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
run bubble test 4
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]

"""