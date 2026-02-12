from checkmate import checkmate


def print_separator():
    print("=" * 60)


def print_piece_patterns():
    print("\n" + "=" * 60)
    print("รูปแบบการเดินของแต่ละตัวหมาก")
    print("=" * 60)
    
    print("\nPawn (P):")
    print(". . . . . . .")
    print(". . . . . . .")
    print(". . X . X . .")
    print(". . . P . . .")
    print(". . . . . . .")
    print(". . . . . . .")
    print(". . . . . . .")
    
    print("\nBishop (B):")
    print("X . . . . . X")
    print(". X . . . X .")
    print(". . X . X . .")
    print(". . . B . . .")
    print(". . X . X . .")
    print(". X . . . X .")
    print("X . . . . . X")
    
    print("\nRook (R):")
    print(". . . X . . .")
    print(". . . X . . .")
    print(". . . X . . .")
    print("X X X R X X X")
    print(". . . X . . .")
    print(". . . X . . .")
    print(". . . X . . .")
    
    print("\nQueen (Q):")
    print("X . . X . . X")
    print(". X . X . X .")
    print(". . X X X . .")
    print("X X X Q X X X")
    print(". . X X X . .")
    print(". X . X . X .")
    print("X . . X . . X")
    
    print_separator()


def print_board(board_string, title):
    print(f"\n{title}")
    print("-" * 30)
    lines = board_string.strip().split('\n')
    for line in lines:
        print(f"  {line}")
    print("-" * 30)


def main():
    print_piece_patterns()
    
    print("\n" + "=" * 60)
    print("ทดสอบโปรแกรม Checkmate")
    print("=" * 60)
    
    board1 = """\
RK..
....
....
....\
"""
    print_board(board1, "Test 1: Rook รุก King (แนวนอน)")
    print("ผลลัพธ์: ", end="")
    checkmate(board1)
    
    board2 = """\
R...
K...
....
....\
"""
    print_board(board2, "Test 2: Rook รุก King (แนวตั้ง)")
    print("ผลลัพธ์: ", end="")
    checkmate(board2)
    
    board3 = """\
B...
....
..K.
....\
"""
    print_board(board3, "Test 3: Bishop รุก King (ทแยง)")
    print("ผลลัพธ์: ", end="")
    checkmate(board3)
    
    board4 = """\
....
.P..
K...
....\
"""
    print_board(board4, "Test 4: Pawn รุก King")
    print("ผลลัพธ์: ", end="")
    checkmate(board4)
    
    board5 = """\
Q...
....
..K.
....\
"""
    print_board(board5, "Test 5: Queen รุก King (ทแยง)")
    print("ผลลัพธ์: ", end="")
    checkmate(board5)
    
    board6 = """\
Q...
....
K...
....\
"""
    print_board(board6, "Test 6: Queen รุก King (แนวตรง)")
    print("ผลลัพธ์: ", end="")
    checkmate(board6)
    
    board7 = """\
R...
P...
.K..
....\
"""
    print_board(board7, "Test 7: Rook ถูก Pawn บล็อก (ไม่รุก)")
    print("ผลลัพธ์: ", end="")
    checkmate(board7)
    
    board8 = """\
R...
.K..
..P.
....\
"""
    print_board(board8, "Test 8: ไม่มีใครรุก King")
    print("ผลลัพธ์: ", end="")
    checkmate(board8)
    
    board9 = """\
..
.K\
"""
    print_board(board9, "Test 9: กระดานเล็ก (ไม่มีใครรุก)")
    print("ผลลัพธ์: ", end="")
    checkmate(board9)
    
    print("\n" + "=" * 60)
    print("สิ้นสุดการทดสอบ")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()