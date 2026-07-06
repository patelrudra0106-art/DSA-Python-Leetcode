class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1

        while top <= bot:
            midR = (top + bot)//2

            if matrix[midR][0] <= target <= matrix[midR][-1]:
                break
            elif matrix[midR][0] > target:
                bot = midR - 1
            else:
                top = midR + 1
        
        left = 0
        right = len(matrix[midR]) -1

        while left <= right :
            mid = (left + right) //2

            if matrix[midR][mid] == target:
                return True
            elif matrix[midR][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False