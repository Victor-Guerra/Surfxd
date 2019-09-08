def shakesort(lis, scores, begin, end):
    if begin >= end:
        return
    #
    for i in range(begin, end - 1):
        if lis[i] > lis[i + 1]: 
            lis[i], lis[i + 1] = lis[i + 1], lis[i]
            scores[i], scores[i + 1] = scores[i + 1], scores[i]
    #
    for k in range(end - 1, begin, -1):
        if lis[k] < lis[k - 1]:
            lis[k], lis[k-1] = lis[k-1],lis[k]
            scores[k], scores[k - 1] = scores[k - 1], scores[k]
    #
    return shakesort(lis, scores, begin+1, end-1)
