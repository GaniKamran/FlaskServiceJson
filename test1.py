from  ipaddress import*
import pprint
z=[]
z=list(ip_network('192.176.0.0/20').hosts())
for i in z:
    print(i)
pprint(z)