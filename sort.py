def shakesort(lis, begin, end):
    if begin >= end:
        return
    #
    for i in range(begin, end - 1):
        if lis[i] > lis[i + 1]: 
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
    #
    for k in range(end - 1, begin, -1):
        if lis[k] < lis[k - 1]:
            lis[k], lis[k-1] = lis[k-1],lis[k]
    #
    return shakesort(lis, begin+1, end-1)
