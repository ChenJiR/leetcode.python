# 240. 搜索二维矩阵 II
# 1504. 面试题04. 二维数组中的查找
# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/


class SearchMatrixSolution:
    def searchMatrix(self, matrix, target):
        x = 0
        y = len(matrix) - 1
        while y >= 0 and x < len(matrix[0]):
            if matrix[y][x] > target:
                y = y - 1
            elif matrix[y][x] < target:
                x = x + 1
            else:
                return True
        return False
