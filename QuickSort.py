def quick_sort(intlist):
    results=[]
    #check in case list has 0 or 1 element
    if len(intlist) <= 1:
        results = intlist
        return results
    
    #define pivot
    pivot = intlist[len(intlist) // 2]
    # create left side
    left = [ x for x in intlist if x < pivot]
    middle = [ x for x in intlist if x == pivot]
    #create right side
    right = [ x for x in intlist if x > pivot]


    return quick_sort(left) + middle + quick_sort(right)



a = [1]
b = [1,2,3,4,5,6]
print(quick_sort(a))
print("Case from tests:")
print(quick_sort([83, 4, 24, 2]))
print("Another case:")
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))