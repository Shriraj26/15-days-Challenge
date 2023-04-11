class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        buff = [None] * n
        isInBuff = [False] * n
        result = []

        def genPermu(buffIndex):

            # Base case
            if buffIndex == len(buff):
                result.append(buff[:])
                return

            for i in range(n):
                if isInBuff[i] == False:
                    # place into the buffer
                    buff[buffIndex] = nums[i]
                    # mark true
                    isInBuff[i] = True
                    # recurse
                    genPermu(buffIndex + 1)
                    # make it False again
                    isInBuff[i] = False
        genPermu(0)

        return result
