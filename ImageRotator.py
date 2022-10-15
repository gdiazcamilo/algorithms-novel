class ImageRotator:

    def rotate(self, matrix: List[List[int]]) -> None:
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while top < bottom:
            self.rotate_rectangle(matrix, top, left, bottom, right)

            top += 1
            left += 1
            bottom -= 1
            right -= 1
    
    def rotate_rectangle(self, matrix, top, left, bottom, right):

        for offset in range(left, right):
            top_left = matrix[top][left + offset]
            top_right = matrix[top + offset][right]
            bottom_right = matrix[bottom][right - offset]
            bottom_left = matrix[bottom - offset][left]

            matrix[top][left + offset] = bottom_left
            matrix[top + offset][right] = top_left
            matrix[bottom][right - offset] = top_right
            matrix[bottom - offset][left] = bottom_right
    