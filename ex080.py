num = []
for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0:
        num.append(val)
    elif c== 1:
        if val > num[0]:
            num.insert(1, val)
        else:
            num.insert(0, val)
    elif c == 2:
        if val > num[0]:
            if val > num[1]:
                num.append(val)
            else:
                num.insert(1, val)
        else:
            num.insert(0, val)
    elif c == 3:
        if val > num[0]:
            if val > num[1]:
                if val > num[2]:
                    num.append(val)
                else:
                    num.insert(2, val)
            else:
                num.insert(1, val)
        else:
            num.insert(0, val)
    elif c == 4:
        if val > num[0]:
            if val > num[1]:
                if val > num[2]:
                    if val > num[3]:
                        num.append(val)
                    else:
                        num.insert(3, val)
                else:
                    num.insert(2, val)
            else:
                num.insert(1, val)
        else:
            num.insert(0, val)
    elif c == 4:
        if val > num[0]:
            if val > num[1]:
                if val > num[2]:
                    if val > num[3]:
                        if val > num[4]:
                            num.append(val)
                        else:
                            num.insert(4, val)
                    else:
                        num.insert(3, val)
                else:
                    num.insert(2, val)
            else:
                num.insert(1, val)
        else:
            num.insert(0, val)
    elif c == 5:
        if val > num[0]:
            if val > num[1]:
                if val > num[2]:
                    if val > num[3]:
                        if val > num[4]:
                            if val > num[5]:
                                num.append(val)
                        else:
                            num.insert(4, val)
                    else:
                        num.insert(3, val)
                else:
                    num.insert(2, val)
            else:
                num.insert(1, val)
        else:
            num.insert(0, val)
print(num)