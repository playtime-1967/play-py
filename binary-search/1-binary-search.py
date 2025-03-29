
arr = [-3, -1, 0, 1, 3, 5]

# traditional way
def binary_search(arr, target: int) -> bool:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + ((right - left) // 2)

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid + 1  

    return False


print("binary_search: ", binary_search(arr, 1))

# ---------- Binary search with condition- such as find number of false
arr2 = [False, False, False, False, True, True, True]

def binary_search_condition(arr) -> int:
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (right + left)//2

        if arr[mid]:
            right = mid
        else:
            left = mid + 1

    return left


print("binary_search_condition: ", binary_search_condition(arr2))
