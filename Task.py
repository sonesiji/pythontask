rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

half_cols = (cols + 1) // 2 if cols % 2 != 0 else cols // 2

def print_top_row(half_cols):
    for _ in range(half_cols):
        print(" ___", end="    ")
    print()

def print_middle_row(half_cols, end_pattern):
    for i in range(half_cols):
        if i != (half_cols - 1):
            print("/   \___", end="")
        else:
            print(end_pattern, end="")
    print()

def print_bottom_row(half_cols, end_pattern):
    for i in range(half_cols):
        if i != (half_cols - 1):
            print("\___/", end="   ")
        else:
            print(end_pattern)

print_top_row(half_cols)

for row in range(rows):
    if cols % 2 != 0:
        print_middle_row(half_cols, "/   \ ")
        print_bottom_row(half_cols, "\___/")
    else:
        print_middle_row(half_cols, "/   \___" if row == 0 else "/   \___/")
        print_bottom_row(half_cols, "\___/    " if row == rows - 1 else "\___/   \ ")
