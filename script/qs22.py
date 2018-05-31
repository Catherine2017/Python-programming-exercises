def bin_search(alist, element):
    start = 0
    end = len(alist) - 1
    index = -1
    while end >= start and index == -1:
        mid = int((start+end)/2)
        #print(start, end, mid)
        if alist[mid] == element:
            index = mid
        elif element > alist[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return index
li = [2,5,7,9,11,17,222]
print(bin_search(li, 11))
print(bin_search(li, 2))
print(bin_search(li, 222))
