import ipinfo
import requests
#https://whatismyv6.com/home.cgi
#import folium
import socket

key = '2a2f20187c8678'#4 ipinfo API

local_ip = socket.gethostbyname(socket.gethostname())
print("Your Local IP:", local_ip)


userIp = requests.get("https://ipinfo.io/ip").text.strip()
print("Your Public IP:", userI, "(may not work)")

ip = input("Enter IPadress for research: ")
handler = ipinfo.getHandler(key)
details = handler.getDetails(ip)
#map =  folium.Map(location=[details.latitude, details.longitude])
print('City: '+details.city)
print('Coordinates: '+details.loc)
