import tester_dictionaries as td

#takes a string and returns the value of the first unit in it
#TODO: simplify these four functions to eliminate repititions 
def unitSize(output_line, dictionary):

    for unit in dictionary:
        if unit in output_line:
            return dictionary[unit]

def transferFormat(transfer_num):

    numLen = int(len(str(int(transfer_num))))

    if numLen % 3 == 0:
        newNum = str(transfer_num / pow(10, numLen - 3))

    else:
        newNum = str(transfer_num / pow(10, numLen - numLen % 3))

    return newNum + td.transferLenToUnit[numLen]

def bandwidthFormat(bandwidth_num):

    numLen = int(len(str(int(bandwidth_num))))

    if numLen % 3 == 0:
        newNum = str(bandwidth_num / pow(10, numLen - 3))

    else:
        newNum = str(bandwidth_num / pow(10, numLen - numLen % 3))

    return newNum + td.bandwidthLenToUnit[numLen]

#TODO: use numpy instead of below function
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)