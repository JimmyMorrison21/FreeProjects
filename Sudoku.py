brckt= [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
def done_or_not(board):
    def done_or_not(board):

        for x in range(9):
            if (
                    # Rows
                    len(set(board[x])) < 9 or
                    # Columns
                    len(set(board[a][x] for a in range(9))) < 9 or
                    # Regions
                    len(set(board[x // 3 * 3 + a // 3][x // 3 * 3 + a % 3] for a in range(9))) < 9
            ):
                # Not valid
                return "Try again!"
        # Valid
        return "Finished!"