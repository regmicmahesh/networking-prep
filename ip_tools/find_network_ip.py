from ip_to_int import ip_to_int
from int_to_ip import int_to_ip

def find_network(subnet, host):
    subnet = ip_to_int(subnet)
    host = ip_to_int(host)
    network = subnet & host
    return network , int_to_ip(network)
