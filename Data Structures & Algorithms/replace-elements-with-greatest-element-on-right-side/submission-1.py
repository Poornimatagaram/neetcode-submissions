class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1

        for i in range(len(arr) -1 , -1 , -1):
            original_val = arr[i]
            arr[i] = max_so_far
            if original_val > max_so_far:
                max_so_far = original_val

        return arr       




        