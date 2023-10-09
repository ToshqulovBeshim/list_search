def find_max_even(d):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    a=0
    ma=d[0]
    while a<len(d):
        if ma<=d[a] and d[a]%2==0:
            ma=d[a]
        a+=1
    return ma
print (find_max_even([2,5,4,6,7,8,5,3,2,1,2,12]))
print (find_max_even([2,5,4,6,7,12,14,17,23]))
