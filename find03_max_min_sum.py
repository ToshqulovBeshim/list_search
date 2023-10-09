def find_max_min_sum(d):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=0
    ma=d[0]
    mi=d[0]
    while a<len(d):
        if ma<=d[a]:
            ma=d[a]
        if mi>=d[a]:
            mi=d[a]
        a+=1
    return ma+mi
print(find_max_min_sum([2,5,7,3,4,6]))
