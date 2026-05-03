class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find possible row
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1

        row = end

        if row < 0:
            return False

        # Binary search inside that row
        start = 0
        end = len(matrix[row]) - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False