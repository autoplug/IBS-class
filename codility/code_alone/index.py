

def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))
