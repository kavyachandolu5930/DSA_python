#quick sort
def quick_sort(a):
    if len(a) <= 1:
        return a
    p = a[0]
    left = [x for x in a if x < p]
    right = [x for x in a if x > p]
    return quick_sort(left) + [p] + quick_sort(right)

print(quick_sort([9, 3, 7, 1, 6]))
