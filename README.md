# NCU-Srun-Python

## 简述 - Description

借鉴了一下前人的代码，给南昌大学的校园网登录系统过写了一个自动化的脚本，使用 `requests` 模拟了一下登录的 HTTP 过程。

## 用法 - Usage

```plaintext
作者本机信息 - Host Info
MacBook Pro (15-inch, 2018) macOS Monterey 12.3.1
Python 3.9.12 (main, Mar 26 2022, 15:51:15)
[Clang 13.1.6 (clang-1316.0.21.2)] on darwin
```

首先，需要确认所依赖的包是否安装：

```plaintext
pip3 install -r requirement.txt
```

安装好依赖项，查看配置文件 `config.json`：

```json
{
    "userInfo": {
        "username": "",
        "password": "",
        "domain": ""
    },
    "platformInfo": {
        "loginURL" : "http://222.204.3.154",
        "device" : "Macintosh",
        "os": "Mac OS"
    }
}
```

按照表格中的进行填入：

| 字段名   | 字段类型 | 应填内容                                      |
| -------- | -------- | --------------------------------------------- |
| username | string   | 登录校园网的用户名                            |
| password | string   | 登录校园网的密码                              |
| domain   | string   | 校园网类型                                    |
| device   | string   | 设备类型（可填：`Machintosh`, `Windows`）     |
| os       | string   | 设备系统（可填：`Mac OS`, `Windows`, `Linux`) |

校园网类型：

| 校园网类型 | 应填内容 |
| ---------- | -------- |
| 中国移动   | cmcc     |
| 中国电信   | ndcard   |
| 中国联通   | unicom   |
| 校园网     | ncu      |

配置好信息之后保存至 `config.json`。

输入：

```plaintext
python3 login.py
```

如果输出：

```
jQuery112405169380394746533_1650453290998({"ServerFlag":0,"ServicesIntfServerIP":"222.204.3.156","ServicesIntfServerPort":"8001","access_token":"09e427ee4c0d9fe79c9af670140e3f00128c9ac7f3fb1dbf33ae3233db2d3192","checkout_date":0,"client_ip":"10.102.195.165","ecode":0,"error":"ok","error_msg":"","online_ip":"10.102.195.165","ploy_msg":"E0000: Login is successful.","real_name":"","remain_flux":0,"remain_times":0,"res":"ok","srun_ver":"SRunCGIAuthIntfSvr V1.18 B20210305","suc_msg":"login_ok","sysver":"1.01.20210305","username":"**********@*","wallet_balance":0})
```

其中：

```
"error":"ok"
```

代表登录成功。

## License

本项目按照 [GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt) 进行开源。

## Credit

[coffeehat/BIT-srun-login-script](https://github.com/coffeehat/BIT-srun-login-script)

[huxiaofan1223/jxnu_srun](https://github.com/huxiaofan1223/jxnu_srun)