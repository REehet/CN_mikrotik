import requests

url = "http://www.iwik.org/ipcountry/mikrotik/CN"

r = requests.get(url).text.replace('CN', 'CN_backup')

with open('CN_backup', 'w') as file:
    file.write(r)
