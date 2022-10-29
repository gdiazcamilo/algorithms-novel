from typing import List


class ImageRotator:
    """
        This class solves the problem: https://leetcode.com/problems/rotate-image/
        
        Assumptions:
            The matrix is n x n

        The problem is solved using an O(1) memory and O(n) runtime approach.
        The approach is to breakdown the matrix into inner squares and rotate the squares from the outermost to the innermost.
        To identify the inner square we use four pointers for the edges (top, left, right, bottom).
        The rotation is made counter-clockwise because this way there's no need to declare a temp variable for each cell of the square:
        freeing the first cell by holding its value in a temp variable and moving the 
        corresponding previous cell (thus freeing the cell) to the next corresponding cell and so on.

    """


    def rotate(self, matrix: List[List[int]]) -> None:
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while top < bottom:
            self.__rotate_square(matrix, top, left, bottom, right)

            top += 1
            left += 1
            bottom -= 1
            right -= 1
    
    def __rotate_square(self, matrix, top, left, bottom, right):

        # The number of iterations is one less than the number of elements in the square
        # because the squares share the edge elements for both columns and rows.
        for offset in range(right - left):
            top_left = matrix[top][left + offset]
            
            matrix[top][left + offset] = matrix[bottom - offset][left]
            matrix[bottom - offset][left] = matrix[bottom][right - offset]
            matrix[bottom][right - offset] = matrix[top + offset][right]
            matrix[top + offset][right] = top_left
    