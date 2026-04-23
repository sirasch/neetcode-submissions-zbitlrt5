class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#Initialise
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
#loop through the board
        for i in range(9):
            for j in range(9):
                #skip if empty
                if board[i][j] == '.':
                    continue
                
                new_num = board[i][j]
                #for boxes, we find the box using mod 3 for row and column
                box_id = (i // 3) * 3 + (j // 3)
#If the number is in a box, column or row of the same index, return false
                if new_num in rows[i] or new_num in cols[j] or new_num in boxes[box_id]:
                    return False

                rows[i].add(new_num)
                cols[j].add(new_num)
                boxes[box_id].add(new_num)

        return True   