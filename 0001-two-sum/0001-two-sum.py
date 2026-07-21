class Solution:
    def twoSum(self, nums, target):

        arr = []

        # store number with index
        for i in range(len(nums)):
            arr.append((nums[i], i))

        # sort array
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:

            s = arr[left][0] + arr[right][0]

            if s == target:
                return [arr[left][1], arr[right][1]]

            elif s < target:
                left += 1

            else:
                right -= 1