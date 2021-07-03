from ip_to_int import ip_to_int


def subnet_to_cidr(subnet):
    subnet = ip_to_int(subnet)
    subnet_bin = bin(subnet)[2:]
    cidr = 0
    for i in subnet_bin:
        if i == "0":
            break
        cidr += 1
    return cidr
