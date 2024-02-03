
def ric_seq(low, high):
    longest = '123456789'
    combos = []

    for can_del in range(len(longest)):
        for el_to_del in range(can_del + 1):
            front = el_to_del
            back = can_del - el_to_del

            trim_str = longest[front:]
            if back:
                trim_str = trim_str[:-back]

            combos.append(int(trim_str))

    combos = sorted(combos)
    return [el for el in combos if low <= el <= high]
