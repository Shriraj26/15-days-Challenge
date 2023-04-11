"""
Process the array from reverse,
You will need 2 passes for that, init the result as -1
if stack is empty, push the index into the stack,
If not, till top of stack is greater than curr elem, pop the elems, 
then set result with top of the stack
push the index of nums to the stack
Refer to the Approach 3 of the editorial for more details
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []

        result = [-1] * len(nums)

        for j in range(2):
            for i in range(len(nums)-1, -1, -1):

                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()

                if stack and nums[stack[-1]] > nums[i]:
                    result[i] = nums[stack[-1]]

                stack.append(i)

        return result
