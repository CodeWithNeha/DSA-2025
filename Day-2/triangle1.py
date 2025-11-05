def fun(row, col):
    if row == 0:
        return 
    if col< row:
        print("*",end="")
        col +=1
        fun(row, col)
    else:
        print()
        row = row-1
        fun(row, 0)


fun(4,0)