def find_min_index(d):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    a=0
    mi=d[0]
    while a<len(d):
        if mi<=d[a]:
            mi=d[a]
            b=a
        a+=1
    return b+1
print (find_min_index([3,45,6,7,65,4,5,6]))

