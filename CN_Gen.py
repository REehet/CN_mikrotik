import requests

url = "https://ispip.clang.cn/all_cn_cidr.txt"
url2 = "https://ispip.clang.cn/all_cn_ipv6.txt"
output = "/log info \"Loading CN address list\"\n/ip firewall address-list remove [/ip firewall address-list find list=CN]\n/ip firewall address-list\n"

r = requests.get(url).text
r2 = requests.get(url2).text

lines = r.splitlines()
for line in lines:
    output += ":do { add address=" + line + " list=CN } on-error={}\n"

output += "/ipv6 firewall address-list remove [/ipv6 firewall address-list find list=CN]\n/ipv6 firewall address-list\n"
    
lines2 = r2.splitlines()
for line2 in lines2:
    output += ":do { add address=" + line2 + " list=CN } on-error={}\n"

with open('CN', 'w') as file:
    file.write(output)

with open('CN_backup', 'w') as file:
    file.write(output.replace('CN', 'CN_backup'))
