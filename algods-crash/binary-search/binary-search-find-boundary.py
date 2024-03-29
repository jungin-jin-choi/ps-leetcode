def find_boundary(arr):
    left, right = 0, len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] and not arr[mid-1]:
            return mid
        elif arr[mid]:
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1

    return boundary_index
