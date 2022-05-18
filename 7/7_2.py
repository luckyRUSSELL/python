def merge_sort(s):
    n = len(s)
    if n == 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return two_list(left, right)

def two_list(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
        i += 1
    if j < len(right):
        result += right[j:]
        j += 1

    return result

a_s = [3, 6, 1, 25, 14, 4]
print(merge_sort(a_s))