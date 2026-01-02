class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        left_boundary = 0
        right_boundary = len(matrix[0]) -1
        top_boundary = 0
        bottom_boundary = len(matrix) -1
        while left_boundary <= right_boundary and top_boundary <= bottom_boundary :
            self.goAround(matrix,left_boundary,right_boundary,top_boundary,bottom_boundary,result)
            left_boundary +=1
            right_boundary -=1
            top_boundary +=1
            bottom_boundary -=1
        return result

    def goAround(self,matrix,left_boundary,right_boundary,top_boundary,bottom_boundary,result):
        column = left_boundary
        # visit all the top row
        while column <= right_boundary:
            result.append(matrix[top_boundary][column])
            column += 1
        # if there is only a single row, no need to do the rest.
        if top_boundary == bottom_boundary:
            return result

        # visit the right column
        row = top_boundary
        while row < bottom_boundary:
            row += 1
            result.append(matrix[row][right_boundary])
        # if there is only a single column, no need to do the rest.
        if left_boundary == right_boundary:
            return result
        # visit the bottom row.
        column = right_boundary
        while column > left_boundary:
            column -=1
            result.append(matrix[bottom_boundary][column])
        # visit the left column
        row = bottom_boundary
        while row > top_boundary+1:
            row -= 1
            result.append(matrix[row][left_boundary])

