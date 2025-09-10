__package__ = "3. Matrix"

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        l = r * c

        ans = []

        left = 0
        right = c - 1
        top = 0
        bottom = r - 1

        while l > 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
                l -= 1
            top += 1

            if l == 0:
                return ans
            
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
                l -= 1
            right -= 1

            if l == 0:
                return ans

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
                l -= 1
            bottom -= 1

            if l == 0:
                return ans

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
                l -= 1
            left += 1

            if l == 0:
                return ans

        return ans


if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []
    print(f"Enter {r} rows with {c} space-separated numbers each:")
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)

    solution = Solution()
    result = solution.spiralOrder(matrix)

    print("\nSpiral Order Traversal:")
    print(result)
