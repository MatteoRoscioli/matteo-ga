white = "@"
black = "#"

def print_chessboard(black, white):
    print("   a  b  c  d  e  f  g  h")
    print("1 " + ("["+black+"]"+"[ ]")*4)
    print("2 " + ("[ ]"+"["+black+"]")*4)
    print("3 " + ("["+black+"]"+"[ ]")*4)
    print("4 " + "[ ]" * 8)
    print("5 " + "[ ]"*8)
    print("6 " + ("[ ]"+"["+white+"]")*4)
    print("7 " + ("["+white+"]"+"[ ]")*4)
    print("8 " + ("[ ]"+"["+white+"]")*4)
    
print(print_chessboard(black, white))

piece_coords = input("Enter piece coordinates (A1-H8):\n").upper()

if piece_coords == "B6:C5":
    print(print_chessboard(black, white))