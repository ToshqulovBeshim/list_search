def find_min(d):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    a=0
    mi=d[0]
    while a<len(d):
        if mi>=d[a]:
            mi=d[a]
        a+=1
    return mi
print (find_min ([3,4,5,8,2]))