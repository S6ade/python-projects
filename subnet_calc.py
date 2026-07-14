import ipaddress
import sys


if len(sys.argv) < 2:
    print("Введите адрес и маску")
else:
    address = sys.argv[1]
    network = ipaddress.IPv4Network(address, strict=False)
    print(f"Адрес сети:     {network.network_address}")
    print(f"Broadcast:      {network.broadcast_address}")
    print(f"Маска:          {network.netmask}")
    print(f"Префикс:        /{network.prefixlen}")
    hosts = list(network.hosts())
    print(f"Первый хост:     {hosts[0]}")
    print(f"Последний хост:  {hosts[-1]}")
    print(f"Количество:      {len(hosts)}")
