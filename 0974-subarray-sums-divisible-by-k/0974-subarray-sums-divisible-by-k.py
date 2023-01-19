class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remainder = defaultdict(int)

        remainder[0] = 1
        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num
            rem = cur_sum % k

            res += remainder[rem]
            remainder[rem] += 1
        
        return res