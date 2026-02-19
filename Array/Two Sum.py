def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(nums)
target= int(input("Enter target: "))

result = twoSum(nums, target)
print("Indices are:", result)