from datetime import datetime
import pyautogui as pg
import pyperclip
import webbrowser
import time


def clickandtype():
    pg.click(1397, 832)
    pg.write('Hello World', interval=0.5)


url = 'http://www.google.com'


def typetosearch():
    webbrowser.open(url)
    time.sleep(5)
    pg.write("What time is it", interval=0.25)
    time.sleep(2)
    pg.press('Enter')


#pyperclip.copy('สวัสดีครับ')


#while True:
#    t = pyperclip.paste()
#    print(t)
#    time.sleep(5)

#t = 'hello'
#old_text = 'hello'
#while True:
#    t = pyperclip.paste()
#    if old_text != t:
#        print(t)
#    time.sleep(1)
#    old_text = t

url = 'http://www.google.com'
webbrowser.open(url)
time.sleep(5)

keyword = 'อุณหภูมิกรุงเทพ'
pyperclip.copy(keyword)
time.sleep(2)

pg.hotkey('ctrl', 'v')
time.sleep(2)

pg.press('enter')
time.sleep(2)

stamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
file = 'capture-{}.png'.format(stamp)
pg.screenshot(file)
