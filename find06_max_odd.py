def find_max_odd(d):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a=0
    ma=d[0]
    while a<len(d):
        if ma<=d[a] and d[a]%2==1:
            ma=d[a]
        a+=1
    return ma
print (find_max_odd ([3,5,7,6,3,9]))