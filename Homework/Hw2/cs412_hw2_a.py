"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def print_board(board):
    for row in board:
        for val in row:
            print(f"{val:02d} ", end="")
        print()


def tile(board, top, left, size, hole_row, hole_col, tile_num):
    if size == 2:
        tile_num += 1
        for row in (top, top + 1):
            for col in (left, left + 1):
                if (row, col) != (hole_row, hole_col):
                    board[row][col] = tile_num
        return tile_num

    half = size // 2
    mid_r, mid_c = top + half, left + half

    # finding hole
    top_half = hole_row < mid_r
    left_half = hole_col < mid_c
    if top_half and left_half:
        hole_quad = 0
    elif top_half and not left_half:
        hole_quad = 1
    elif not top_half and left_half:
        hole_quad = 2
    else:
        hole_quad = 3

    # center positions
    centers = {
        0: (mid_r - 1, mid_c - 1),
        1: (mid_r - 1, mid_c),
        2: (mid_r, mid_c - 1),
        3: (mid_r, mid_c),
    }

    tile_num += 1
    for q in range(4):
        if q != hole_quad:
            row, col = centers[q]
            board[row][col] = tile_num

    # going into each quadrant
    tl_hole = (hole_row, hole_col) if hole_quad == 0 else centers[0]
    tile_num = tile(board, top, left, half, tl_hole[0], tl_hole[1], tile_num)

    tr_hole = (hole_row, hole_col) if hole_quad == 1 else centers[1]
    tile_num = tile(board, top, left + half, half,
                    tr_hole[0], tr_hole[1], tile_num)

    bl_hole = (hole_row, hole_col) if hole_quad == 2 else centers[2]
    tile_num = tile(board, top + half, left, half,
                    bl_hole[0], bl_hole[1], tile_num)

    br_hole = (hole_row, hole_col) if hole_quad == 3 else centers[3]
    tile_num = tile(
        board, top + half, left + half, half, br_hole[0], br_hole[1], tile_num
    )

    return tile_num


def main():
    n = int(input().strip())
    size = 2**n
    hole_row, hole_col = map(int, input().split())

    # making the empty board
    board = [[0 for _ in range(size)] for _ in range(size)]
    board[hole_row][hole_col] = -1

    # filling board
    tile(board, 0, 0, size, hole_row, hole_col, -1)
    print_board(board)


if __name__ == "__main__":
    main()
