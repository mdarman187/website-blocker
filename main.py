import time
from datetime import datetime as dt

hp = r"C:\Windows\System32\drivers\hosts"   #provide the proper host path according to yor system
redirect = "127.0.0.1"
web = ["www.youtube.com","www.facebook.com"]  #add the website links in the list

while True:
  if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
    print("Sorry you are not allowed...")
    with open(hp,'r+') as file:
      content = file.read()
      for site in web:
        if site in content:
          pass
        else:
          file.write(redirect+" "+site+"\n")
  else:
    with open(hp,'r+') as file:
      content = file.readlines()
      file.seek(0)
      for line in content:
        if not any(site in line for site in web):
          file.write(line)
      file.truncate()
    print("Access Granted....")
  time.sleep(5)
