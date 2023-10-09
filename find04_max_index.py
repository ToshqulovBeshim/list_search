def find_max_index(d):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    a=0
    ma=d[0]
    while a<len(d):
        if ma<=d[a]:
            ma=d[a]
            b=a
        a+=1
    return b+1
print (find_max_index([2,3,5,6,7,4,2,2,3,4,6,6]))
