# Проект: Калькулятор IP-подсетей
# Цель: По заданному IP-адресу с маской вычислить параметры сети
# Использование: python3 subnet_calc.py 192.168.1.15/24

import ipaddress  # для работы с IP-адресами и сетями
import sys        # для аргументов командной строки


# Проверяем, что пользователь передал адрес
if len(sys.argv) < 2:
    print("Введите адрес и маску (например, 192.168.1.15/24)")
else:
    # Получаем адрес из аргументов
    address = sys.argv[1]

    # Создаём объект сети (strict=False позволяет передавать адрес хоста)
    network = ipaddress.IPv4Network(address, strict=False)

    # Выводим основные параметры сети
    print(f"Адрес сети:     {network.network_address}")
    print(f"Broadcast:      {network.broadcast_address}")
    print(f"Маска:          {network.netmask}")
    print(f"Префикс:        /{network.prefixlen}")

    # Получаем список всех доступных хостов
    hosts = list(network.hosts())

    # Выводим первый, последний и общее количество
    print(f"Первый хост:     {hosts[0]}")
    print(f"Последний хост:  {hosts[-1]}")
    print(f"Количество:      {len(hosts)}")
