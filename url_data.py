import time
import requests

name = 'nginx'
url = 'http://127.0.0.1:5000/server/%s'%name

# while True:
#     run = requests.get(url=url).json()
#     data = run['servers']
#     print("上传：",data[1]['network_tx'] / 1024,"Kb")
#     print("下载：",data[1]['network_rx'] / 1024,"Kb")
#     time.sleep(1)
#     print("="*100)

run = requests.get(url=url)
print(run.text)