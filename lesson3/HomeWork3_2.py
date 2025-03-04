
nums = [12, 3, 4, 10, 8]

if len(nums) > 0:
    nums = [nums[-1]] + nums[:-1]

print(nums)
