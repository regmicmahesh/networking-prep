conf = {
    "0": "---",
    "1": "--x",
    "2": "-w-",
    "3": "-wx",
    "4": "r--",
    "5": "r-x",
    "6": "rw-"
}

rev_conf = {x: y for y, x in conf.items()}


def converter(perm: str):
    if perm.strip().isdigit():
        str_perm = map(lambda x: conf[x], perm)
        return "".join(str_perm)
    else:
        digit_perm = (rev_conf[perm[x:x+3]] for x in range(0, 9, 3))
        return "".join(digit_perm)


if __name__ == "__main__":
    import sys
    print(converter(sys.argv[1]))

