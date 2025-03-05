import ipinfo
import requests
#https://whatismyv6.com/home.cgi
#import folium


key = '2a2f20187c8678'#4 ipinfo API



userData = requests.get("https://ipinfo.io/json").json()
ipv6 = requests.get("https://api64.ipify.org").text.strip()

print("Here is your public IPv4 data: ")
print(f"IP: {userData['ip']}, City: {userData['city']}, Region: {userData['region']}, Country: {userData['country']}")
print("**Your Data may be going through a cloud server**")


ip = input("Enter costom IP address for research: ")
handler = ipinfo.getHandler(key)
details = handler.getDetails(ip)
#map =  folium.Map(location=[details.latitude, details.longitude])
print('City: '+details.city)
print('Country:'+details.country)
print ('Region:'+details.region)
print('Coordinates: '+details.loc)
