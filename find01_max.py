def find_max(d):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    a=0
    ma=d[0]
    while a<len(d):
        if ma<=d[a]:
            ma=d[a]
        a+=1
    return ma
print(find_max([1,3,4,2,7,5]))
    