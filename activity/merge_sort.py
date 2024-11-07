from .mergelib import merge_sorted

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.

def merge_sort(data):
    # If the list is 0 or 1 long, it's trivially sorted.
    # Make a copy in case this was the original input
    # (We don't want to return a reference to the input data.
    # The returned list should always be a new list.)
    if len(data) <= 1:
        return list(data)

    # Split the array into two halves
    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:]

    sorted_left = merge_sort(left)  # Merge sort the front half
    sorted_right = merge_sort(right)  # Merge sort the rear half

    # Combine the two sorted halves
    sorted_data = merge_sorted(sorted_left, sorted_right)

    # Return the now sorted array
    return sorted_data

# The same code as above, but condensed
    
# def merge_sort(data):
#     if len(data) <= 1:
#         return list(data)
    
#     mid = len(data) // 2
#     return merge_sorted(merge_sort(data[0:mid]), merge_sort(data[mid:]))
