# Put your function here
def decreaseElements(nums):
    for i in range(len(nums)):
            for j in range(len(nums[i])):
                print(nums[i][j]-1, end = " ")

# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
decreaseElements(nums)