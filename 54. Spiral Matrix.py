"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""


def spiral_order(matrix):
    res = []
    start_col = start_row = 0
    end_col, end_row = len(matrix[0]) - 1, len(matrix) - 1
    while start_col <= end_col and start_row <= end_row:
        for i in range(start_col, end_col + 1):
            res += [matrix[start_row][i]]
        start_row += 1
        for i in range(start_row, end_row + 1):
            res += [matrix[i][end_col]]
        end_col -= 1

        if len(res) < len(matrix) * len(matrix[0]):
            for i in range(end_col, start_col - 1, -1):
                res += [matrix[end_row][i]]
            end_row -= 1
        if len(res) < len(matrix) * len(matrix[0]):
            for i in range(end_row, start_row - 1, -1):
                res += [matrix[i][start_col]]
            start_col += 1
    return res


user_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral_order(matrix=user_matrix))
