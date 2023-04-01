

import time
from datetime import datetime as dt
website_list=["www.facebook.com","www.instagram.com","https://facebook.com","https://instagram.com","www.youtube.com","https://youtube.com"]
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,20)<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,21):
        print("Focus Mode On!!!")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Chilling!!!")
    time.sleep(2)
    
