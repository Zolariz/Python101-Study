import random

name = 'Sorn'
print(name)
type(name)
friend = 'สมชาย'
print('สวัสดี สมชาย สบายดีไหม?')
print('สวัสดี ' + friend + ' สบายดีไหม?')
money = 10
print('สมชายยืมเงิน 10 บาท')

print(friend + 'ยืมเงิน ' + str(money) + ' บาท')

print('{}ยืมเงิน {} บาท'.format(friend, money))
print(f'{friend}ยืมเงิน {money} บาท')

money = 1543212315412
print(f'{money:,}')
print(f'{money:,.2f}')
print('{:,.2f}'.format(money))

random.randint(1, 7)

store = ['ป้าส้ม', 'ป้าเล็ก', 'ลุงดำ']
random.choice(store)