import platform

if platform.system() == "Windows":
        pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
        pathToHosts=r"/etc/hosts"

redirect="127.0.0.1"
websites=["https://google.com/","https://abv.com/","https://www.xn.com/","https://www.videos.com/","https://www.hub.com/"]

with open(pathToHosts,'r+') as file:
    content=file.read()
    for site in websites:
        if site in content:
            pass
        else:
            file.write(redirect+" "+site+"\n")
            
