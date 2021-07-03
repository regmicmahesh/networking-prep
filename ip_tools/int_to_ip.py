def int_to_ip(num: int):
    result = ""
    for i in [24,16,8,0]:
        #0xFF is used to mask only last 8bits.
        result += str(num >> i & 0xFF) + "."
    return result[:-1]
