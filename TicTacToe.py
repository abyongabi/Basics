l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sel = []
win = False

while not win:
    for i in l:
        for k in i:
            print(str(k) + " ", end="")
        print()
    num = int(input("Enter a number: "))
    for i in range(len(l)):
        for k in range(len(l[i])):
            if l[i][k] == num:
                sel.append(num)
                l[i][k] = 'X'
        if len(sel) >= 3:
            diff = []
            for i in sel:
                for k in sel:
                    if k - i in diff:
                        win = True
                    elif k - i != 0:
                        diff.append(k - i)

    if win:
        for i in l:
            for k in i:
                print(str(k) + " ", end="")
            print()
        print("Win")
