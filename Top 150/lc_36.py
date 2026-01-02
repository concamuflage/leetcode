
from typing import List
#
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         return self.isValidCrossTotal(board)&self.isValidRow(board)&self.isValidColumn(board)
#
#     def isValidCross(self,index1,index2,board):
#         # to check if a 3*3 area is valid
#         dic = [0] * 9
#         for number1 in range(3):
#             for number2 in range(3):
#                 element = board[index1 + number1][index2 + number2]
#                 if element != ".":
#                     if dic[int(element)-1] == 1:
#                         return False
#                     else:
#                         dic[int(element)-1] = 1
#         return True
#     def isValidCrossTotal(self, board: List[List[str]]) -> bool:
#         n = len(board)
#         for index1 in range(0,n,3):
#             for index2 in range(0,n,3):
#                 if not self.isValidCross(index1,index2,board):
#                     return False
#         return True
#
#     def isValidRow(self,board):
#         for row in board:
#             dict = [0]*len(board)
#             for index,element in enumerate(row):
#                 if element != ".":
#                     if dict[int(element)-1] == 1:
#                         return False
#                     else:
#                         dict[int(element)-1] = 1
#         return True
#
#     def isValidColumn(self,board):
#         for column in range(len(board)):
#             dict = [0] * len(board)
#             for row in board:
#                 element = row[column]
#                 if element != ".":
#                     if dict[int(element)-1] == 1:
#                         return False
#                     else:
#                         dict[int(element)-1] = 1
#         return True

#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # GPT solution is so concise.
        # O(n) solution, n is the number of cells on the board
        # the key is to know index = (row // 3) *3 + column // 3 will index into the correct box
        # if the sub boxes are indexed as
        # 0 1 2
        # 3 4 5
        # 6 7 8
        # (row // 3) * 3 will index into the correct row
        # column // 3 will move the index to the right


        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                element = board[row][column]
                if element != ".":
                    # check if it is duplicate in its row
                    row_set = rows[row]
                    # check if it is duplicate in its column
                    column_set = columns[column]
                    # check if it is duplicate in its box
                    box_number = (row // 3) *3 + column // 3
                    box_set = boxes[box_number]
                    if element in box_set or element in row_set or element in box_set:
                        return False
                    row_set.add(element)
                    column_set.add(element)
                    box_set.add(element)

        return True



sol = Solution()

# board3 = [
#     [1,2,1],
#     [2,1,2],
#     [0,2,3]
# ]
# # print(sol.isValidRow(board3)) # false
# # print(sol.isValidColumn(board3)) # false
# print(sol.isValidCross(0,0,board3)) # False
#
# board4 = [
#     [1,2,3],
#     [0,1,7],
#     [4,5,6]
# ]
# # print(sol.isValidRow(board3)) # true
# # print(sol.isValidColumn(board3)) # true
# print(sol.isValidCross(0,0,board4)) # False
#
# board5 = [
#     ["3","2","1"],
#     ["4",".","5"],
#     ["6","7","8"]
# ]
# print(sol.isValidCross(0,0,board5)) # true


board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(sol.isValidSudoku(board1))          # true
print(sol.isValidSudoku(board2))          # false

