from find_network_ip import find_network

def check_if_same_network(ip1, subnet, ip2):

    net1 = find_network(subnet, ip1)[0]
    net2 = find_network(subnet, ip2)[0]
    return net1 == net2

