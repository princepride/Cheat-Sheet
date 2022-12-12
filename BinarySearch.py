class Solution:
    def searchRange(self, nums, target ):
        #find the starting position of a given target value by binarySearch
        def binarySearch1(nums, target):
            start = 0
            end = len(nums) - 1
            res = -1
            while start <= end :
                mid = start + (end - start) //2
                if nums[mid] == target:
                    res = mid
                    end = mid - 1
                elif nums[mid] < target :
                    start = mid +1
                else:
                    end = mid -1
            return res
                
        #find the ending position of a given target value by binarySearch
        def binarySearch2( nums, target):
            start = 0
            end = len(nums) - 1
            res = -1
            while start <= end :
                mid = start + (end - start) //2
                if nums[mid] == target:
                    res = mid
                    start = mid +1
                elif nums[mid] < target :
                    start = mid +1
                else:
                    end = mid -1
            return res

        #just binarySearch
        def binarySearch3(nums, target):
            start = 0
            end = len(nums) - 1
            while start <= end :
                mid = start + (end - start) //2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target :
                    start = mid +1
                else:
                    end = mid -1
            return -1
        return [binarySearch1(nums,target), binarySearch2(nums,target)]

        #find leftmost binary search





        # find rightmost binary search