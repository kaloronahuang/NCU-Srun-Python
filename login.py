# login.py
import json
import requests
import urllib.parse
import re

from encryption import srun_base64, srun_md5, srun_sha1, srun_xencode

loginURL = ''
enc = 's' + 'run' + '_bx1'
n = 200
type_num = 1
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}

def readConfig():
    global loginInfo, loginURL, header, device, os
    configFile = open('config.json')
    configInfo = json.loads(str(configFile.read()))
    loginInfo = configInfo['userInfo']
    loginURL = configInfo['platformInfo']['loginURL']
    device = configInfo['platformInfo']['device']
    os = configInfo['platformInfo']['os']

def getInfo():
    resp = requests.get(loginURL)
    current_url = resp.url
    resp_info = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(current_url).query))
    loginInfo['ac_id'] = resp_info['ac_id']
    loginInfo['double_stack'] = 0
    loginInfo['otp'] = False
    fpos = resp.text.find('<input type=\"hidden\" name=\"user_ip\" id=\"user_ip\" value=\"') + 56
    segment = resp.text[fpos:fpos + 15]
    loginInfo['ip'] = re.match(r"[0-9]+.[0-9]+.[0-9]+.[0-9]+", segment).group()

def getChallenge(data):
    data['callback'] = 'jsonp1583251661367'
    return requests.get(loginURL + '/cgi-bin/get_challenge', params=data, headers=header)

def getPortal(data):
    return requests.get(loginURL + '/cgi-bin/srun_portal', params=data, headers=header)

def info(d, k):
    return '{SRBX1}' + srun_base64.get_base64(srun_xencode.get_xencode(json.dumps(d), k))

def login():
    username = loginInfo['username'] + '@' + loginInfo['domain']
    params = {'username': username, 'ip': loginInfo['ip']}
    resp = getChallenge(params)
    token = re.search('"challenge":"(.*?)"', resp.text).group(1)
    payload = {
        'username':username,
        'password':loginInfo['password'],
        'ip':loginInfo['ip'],
        'acid':loginInfo['ac_id'],
        'enc_ver': enc
        }
    encoded_payload = info(payload, token)
    hmd5 = srun_md5.get_md5(loginInfo['password'], token)
    chkstr = token + username
    chkstr += token + str(hmd5)
    chkstr += token + loginInfo['ac_id']
    chkstr += token + loginInfo['ip']
    chkstr += token + str(n)
    chkstr += token + str(type_num)
    chkstr += token + encoded_payload
    loginInfo['password'] = '{MD5}' + hmd5
    
    params = {
        'callback': 'jQuery112405169380394746533_1650453290998',
        'action': 'login',
        'username': username,
        'password': loginInfo['password'],
        'ac_id': loginInfo['ac_id'],
        'ip': loginInfo['ip'],
        'chksum': srun_sha1.get_sha1(chkstr),
        'info': encoded_payload,
        'n': n,
        'type': type_num,
        'os':os,
        'name': device,
        'double_stack': 0
    }
    resp = getPortal(params)
    print(resp.text)

def main():
    readConfig()
    getInfo()
    login()

if __name__ == '__main__':
    main()