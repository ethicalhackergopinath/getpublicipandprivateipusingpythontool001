
import socket 
import requests

#pip install request

#Get private ip

hostName = socket.gethostname()
print(hostName)
ipAddr = socket.gethostbyname(hostName)
print(ipAddr)

#get public ip

ipAdd =requests.get('https://api.ipify.org').text
print(ipAdd)

