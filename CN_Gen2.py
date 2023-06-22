import requests

url = "https://ispip.clang.cn/all_cn_cidr.txt"
r = requests.get(url).text

lines = r.splitlines()

output = "/log info \"Loading CN address list\"\n/ip route remove [find comment=\"CN\"]\n/ip route\n"

for line in lines:
    # address = line.split(" ")[1]
    address = line
    output += ":do { add dst-address=" + address + " gateway=192.168.50.1 distance=10 comment=\"CN\" } on-error={}\n"

with open('CN_route', 'w') as file:
    file.write(output)

with open('CN_route_backup', 'w') as file:
    file.write(output.replace('CN', 'CN_backup').replace('distance=10', 'distance=20'))
