
def min_max(arr, low, high):

    if not arr:
        return None
    
    if low == high:
        return arr[low], arr[high]
    
    if low == high - 1:
        return min(arr[low], arr[high]), max(arr[low], arr[high])
    
    mid = low + (high - low) // 2

    left_min, left_max = min_max(arr, low, mid)
    right_min, right_max = min_max(arr, mid+1, high)

    if left_min < right_min:
        fin_min = left_min
    else:
        fin_min = right_min
    
    if right_max < left_max:
        fin_max = left_max
    else:
        fin_max = right_max

    return fin_min, fin_max


array = [1, 2, 3, 4, 56, 75, -5]
low = 0
high = len(array) - 1
print(min_max(array, low, high))

