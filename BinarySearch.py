# Find the starting position of a given target value
def findStartIndex(nums, target):
    start, end = 0, len(nums) - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            res = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res
        
# Find the ending position of a given target value
def findEndIndex(nums, target):
    start, end = 0, len(nums) - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            res = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res
