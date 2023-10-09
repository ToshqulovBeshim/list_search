def find_min_even(d):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    a=0
    mi=d[0]
    while a<len(d):
        if mi<=d[a] and d[a]%2==0:
            mi=d[a]
        a+=1
    return mi
print(find_min_even([67,4567,345,3456,456789]))

