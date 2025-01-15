from ipaddress import ip_address
import socket

host = input("masukkan nama domain : ")
ip_address = socket.gethostbyname(host)

print(f"nama domain : {host}")
print(f"ip Address : {ip_address}")
