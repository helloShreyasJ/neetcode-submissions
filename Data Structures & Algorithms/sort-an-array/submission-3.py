class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort Big-O: O(n^2)    not ideal
        # algo: run through the numbers skipping the first numbers
                                                # idx 0
        # mark current loop counter as the value we're inserting the sorted value insert_at
        # mark current value as the current value
        # in the inner loop; loop from last to first and check:
                # is the element in the inner loop greater than the value we're at in the outer loop:
                        # if true then make change to insert at index val. make it the stuff we're comapring with
                # insert value from the outer loop into the insert at index
                
        # awesomesauce!
                    
        for i in range(1, len(nums)):
            insert_at = i
            current_value = nums.pop(i)
            for j in range(i - 1, -1, -1):
                if nums[j] > current_value:
                    insert_at = j
            nums.insert(insert_at, current_value)

        return nums