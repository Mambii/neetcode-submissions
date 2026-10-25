class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(arr):
            seen = set()
            for item in arr:
                if item == '.':
                    continue
                if item in seen:
                    return True
                seen.add(item)
            return False
        
        for i in range(9):
            test = []
            if(has_duplicates(board[i])):
                return False

            for k in range(9):
                test.append(board[k][i])
            if(has_duplicates(test)):
                return False

        for row_off in range(0,9,3):
            for col_off in range(0,9,3):
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[row_off+r][col_off+c])
                if(has_duplicates(box)):
                    return False
        return True
        

