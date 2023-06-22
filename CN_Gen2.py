import requests

url = "https://ispip.clang.cn/all_cn_cidr.txt"
r = requests.get(url).text

# with open("routes4.conf") as f:
#     lines = f.read().splitlines()

lines = r.splitlines()

output = "/log info \"Loading foreign address list\"\n/ip route remove [find comment=\"foreign\"]\n/ip route\n"

for line in lines:
    # address = line.split(" ")[1]
    address = line
    output += ":do { add dst-address=" + address + " gateway=10.10.70.1 distance=10 comment=\"foreign\" } on-error={}\n"

with open('foreign_route', 'w') as file:
    file.write(output)

with open('foreign_route_backup', 'w') as file:
    file.write(output.replace('foreign', 'foreign_backup').replace('distance=10', 'distance=20'))
