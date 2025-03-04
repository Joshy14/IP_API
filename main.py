import ipinfo
import folium
key = '2a2f20187c8678'
ip = input("Enter IPadress for research: ")
handler = ipinfo.getHandler(key)
details = handler.getDetails(ip)
map =  folium.Map(location=[details.latitude, details.longitude])
map
print('City: '+details.city)
print('Coordinates: '+details.loc)