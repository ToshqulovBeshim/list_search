def find_min_odd(d):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    a=0
    mi=d[0]
    while a>len(d):
        if mi<=d[a] and d[a]%2==1:
            mi=d[a]
        a+=1
    return mi
print(find_min_odd([1,4,3,5,7,9,14,31]))

