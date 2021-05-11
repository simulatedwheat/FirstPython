# use shift enter on highlighted code
#print("Hello")
# def search (x, nums):
#     # nums is a list of numbers and x is a number
#     # Returns the position in the list where x occurs or -1 if
#     # x is not in the list
#     try:
#         return nums.index(x)
#     except:
#         return -1
# print(search(1,[1,2,3,4]))

# Linear search
# Iterate through a list and stop when the desired value is found
# If the desired value is never found, return -1
def linearSearch (x, nums):
    for i in range (len (nums)):
        if nums[i] == x:
            print("The desired value was ", x, " and it was found at index ", i)
            return i
    return -1

# Binary Search
# Takes the middle value and compares it to the desired value
# If desired value is greater than the middle value then the low is 
# assigned the middle value. Then compares the middle of the new range 
# to the desired value. If the desired value is smaller then the new high 
# is the old middle value...

numList = list(range(1, 101))          # Set numList equal to a list of the first 100 integers

def binarySearch (x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:              # There is still a range to search
        mid = (low + high) // 2     # Position of the middle item
        item = nums[mid]
        if x == item :              # The desired value was found
            return mid
        elif x < item :             # x is in the lower half of the range
            high = mid -1           # Move top marker down
        else:                       # x is in upper half
            low = mid + 1           # Move bottom marker up
    return -1                       # x is not in the list

# Test cases to test the algorithm, compares an expected result to the actual result
def testCaseBinary(testNumber, x, nums, expectedResult):
    actualResult = binarySearch(x, nums)
    if actualResult == expectedResult:
        print("Test", testNumber, "Passed")
    else:
        print("Test", testNumber, "Failed. Expected", expectedResult, "But Found", actualResult)

def testBinary():
    testCaseBinary(1, 70, numList, 69)
    testCaseBinary(2, 30, numList, 29)
    testCaseBinary(3, 101, numList, -1)
