def qian_tao():
    row = 1
    while row <= 5:

        col = 1
        while col <= row:
            print("*", end="")
            # print("col=%d" % col)
            col += 1

        # print("row=%d" % row)
        print("")
        row += 1
