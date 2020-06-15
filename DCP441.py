def ThreeArraysDivider(lst, pivot):
    lower = []
    equal = []
    larger = []
    for x in lst:
        if x < pivot:
            lower.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            larger.append(x)
    return lower+equal+larger

arr = [4,7,9,11,10,2,3,55]
piv = 10
finalArr = ThreeArraysDivider(arr, piv)
print(finalArr)