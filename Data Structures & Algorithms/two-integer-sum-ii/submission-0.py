class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            num_fixed = numbers[i]
            for j in range(i, len(numbers)):
                num_running = numbers[j]
                if num_fixed + num_running == target:
                    return  [i+1, j+1]

        