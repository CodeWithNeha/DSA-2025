def fun(row, col):
    if row == 0:
        return 
    if col< row:
        col +=1
        fun(row, col)
        print("*",end="")

    else:
        row = row-1
        fun(row, 0)
        print()



fun(4,0)