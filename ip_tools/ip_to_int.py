def ip_to_int(ip: list[str]):
    result = 0
    nums = ip.split(".")
    nums = map(int, nums)
    for i,v in enumerate(nums):
        """
        push the ip in such a way left shift such taht
        first octate << 24
        second octate << 16
        third octate << 8
        fourth octae << 0
        """
        result += v << ( 8*(3-i))
    return result



