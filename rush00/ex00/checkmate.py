def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                return (row, col)
    return None


def is_valid_position(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[row]):
        return False
    return True


def check_pawn(board, king_row, king_col):
    directions = [(-1, -1), (-1, 1)]
    
    for dr, dc in directions:
        new_row = king_row + dr
        new_col = king_col + dc
        
        if is_valid_position(board, new_row, new_col):
            if board[new_row][new_col] == 'P':
                return True
    
    return False


def check_rook(board, king_row, king_col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc
        
        while is_valid_position(board, row, col):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':
                if piece == 'R':
                    return True
                break
            
            row += dr
            col += dc
    
    return False


def check_bishop(board, king_row, king_col):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc
        
        while is_valid_position(board, row, col):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':
                if piece == 'B':
                    return True
                break
            
            row += dr
            col += dc
    
    return False


def check_queen(board, king_row, king_col):
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    
    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc
        
        while is_valid_position(board, row, col):
            piece = board[row][col]
            
            if piece != '.' and piece != ' ':
                if piece == 'Q':
                    return True
                break
            
            row += dr
            col += dc
    
    return False


def checkmate(board_string):
    board = board_string.strip().split('\n')
    
    if len(board) == 0:
        print("Fail")
        return
    
    board_size = len(board)
    for row in board:
        if len(row) != board_size:
            print("Fail")
            return
    
    king_pos = find_king(board)
    
    if king_pos is None:
        print("Fail")
        return
    
    king_row, king_col = king_pos
    
    if check_pawn(board, king_row, king_col):
        print("Success")
        return
    
    if check_rook(board, king_row, king_col):
        print("Success")
        return
    
    if check_bishop(board, king_row, king_col):
        print("Success")
        return
    
    if check_queen(board, king_row, king_col):
        print("Success")
        return
    
    print("Fail")