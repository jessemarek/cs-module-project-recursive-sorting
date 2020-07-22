# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # find the mid point
    mid = start + end // 2

    # if start is less than the end then we still have values to look at
    if start <= end:
        # if the target is at the mid return
        if arr[mid] == target:
            return mid

        # perform binary_search on the left side
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # perform binary_search on the right side
        else:
            return binary_search(arr, target, mid + 1, end)

    # the target is not in the array
    else:
        return -1

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
