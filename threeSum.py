
def threeSumHasDuplicates(nums):

#SUPER SLOW AND DOESN'T ACCOUNT FOR DUPLICATES
def threeSumHasDuplicates(nums):
    #If length of nums is less than three, we just return empty array
    answerArr = []
    if len(nums) < 3:
        return answerArr
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    answerArr.append([nums[i], nums[j], nums[k]])
    return answerArr

nums = [-1,0,1,2,-1,-4] #[-4, -1, -1, 0, 1, 2]
print(threeSum(nums))
#[[-1,-1,2],[-1,0,1]]

nums = []
print(threeSum(nums))
#[[-1,-1,2],[-1,0,1]]

nums = [0]
print(threeSum(nums))
#[]