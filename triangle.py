
# Maximum path sum in a triangle

#Reference: CodeSavant. (2021). Find the maximum path sum of a triangle in Python. YouTube. Retrieved from https://www.youtube.com/watch?v=v0fR9xPEbEk

def maxPathSum(tri):
    totalRow = len(tri)
    # here using Bottom-Up Approach of DP
    #dp =[[0] * len(row) for row in tri]

    '''
    Please fill in your answer to replace the "?" in the code block
    '''
    for row in range(totalRow -2, -1, -1):
        for col in range(len(tri[row])):
            tri[row][col] += max(tri[row+1][col], tri[row+1][col+1])
    return tri[0][0]

# Test case #1: output = 30 (=7+3+8+7+5)
print(maxPathSum([
        [7],
       [3,8],
      [8,1,0],
     [3,7,4,4],
    [4,5,2,6,5]
]))

# Test case #2: output = 23 (=3+7+4+9)
print(maxPathSum([
       [3],
      [7,4],
     [2,4,6],
    [8,5,9,3]
]))

# Test case #3: output = 21 (=8+-3+8+8)
print(maxPathSum([
       [8],
     [-3,2],
     [8,2,6],
    [1,8,1,1]
]))
