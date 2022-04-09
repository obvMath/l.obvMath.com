# This is used on the backend to create short links.

import random
import string
import os
import pyperclip
import time

url = input('URL to redirect to: ')
print(' ')
backhalf = input('Backhalf (inputing "random" will create a 4 character random backhalf consisting of uppercase letters, lowercase letters, and digits.): ')

if backhalf == "random":
    randomBackhalf = ( ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(4)) )
    os.mkdir(randomBackhalf)
    file = open(f"{randomBackhalf}/index.html","w+")
    file.write(f'<meta http-equiv="refresh" content="0; URL={url}">')
    file.close()
    print(' ')
    print(f'A short link created at "https://x.obvMath.com/{randomBackhalf}". The short link has been copied to the clipboard.')
    pyperclip.copy(f"https://x.obvMath.com/{randomBackhalf}")
else:
    os.mkdir(backhalf)
    file = open(f"{backhalf}/index.html","w+")
    file.write(f'<meta http-equiv="refresh" content="0; URL={url}">')
    file.close()
    print(' ')
    print(f'A short link created at "https://x.obvMath.com/{backhalf}". The short link has been copied to the clipboard.')
    pyperclip.copy(f"https://x.obvMath.com/{backhalf}")

print(' ')
print('Closing in:')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Closing...')