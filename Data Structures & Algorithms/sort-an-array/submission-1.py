class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort Big-O: O(n^2)    not ideal

        for i in range(1, len(nums)):
            insert_at = i
            current_value = nums.pop(i)
            for j in range(i - 1, -1, -1):
                if nums[j] > current_value:
                    insert_at = j
            nums.insert(insert_at, current_value)

        return nums