provinces = {
    'Sichuan': 'Chengdu',
    'Yunnan': 'Qujing',
    'Guangdong': 'Shenzhen'
}

regions = {
    'Sichuan': 'west China',
    'Yunnan': 'southwest China',
    'Guangdong': 'east China'
}

for province, city in provinces.items():
    print(f"{province} has {city}.")
    print(f"{province} is in {regions[province]}.")


