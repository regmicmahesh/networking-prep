
from int_to_ip import int_to_ip

def cidr_to_subnet(cidr):
    breakpoint()
    subnet = "1" * cidr
    subnet = int(subnet.zfill(32)[::-1] , 2)

    return int_to_ip(subnet)
    


