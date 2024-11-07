# do not modify
# merge_sorted may be used in merge_sort implementation

def merge_sorted(left, right):
    merged = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        lval = left[l]
        rval = right[r]

        if lval <= rval:
            merged.append(lval)
            l += 1
        else:
            merged.append(rval)
            r += 1

    # one of these 2 is empty
    merged.extend(left[l:])
    merged.extend(right[r:])

    return merged
