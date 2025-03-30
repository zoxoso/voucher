import requests
import json

with open('data.json', 'r') as file:
    vouchers = json.load(file)

# กำหนด header
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'language_code=th'
}

goodcode = []

url = 'https://potico.co.th/api/apply-voucher-code' 

for voucher in vouchers:
    response = requests.post(url, json=voucher, headers=headers)
    
    content_type = response.headers.get('Content-Type', '')

    if 'application/json' in content_type:
        # หาก Content-Type เป็น application/json แสดงว่า voucher นี้ใช้งานไม่ได้
        print(f"Voucher {voucher['voucher_code']} is invalid.")
        continue
    else:
        # หาก Content-Type ไม่ใช่ application/json แสดงว่า voucher นี้ใช้งานได้
        goodcode.append(voucher['voucher_code'])
        print(f"Voucher {voucher['voucher_code']} is valid.")

print("\nValid vouchers:")
print(goodcode)
