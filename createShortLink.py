# This is used on the backend to create short links.

import random
import string
import os
import pyperclip
import time

url = input('URL to redirect to: ')

isdir = True

while isdir == True:
    print(' ')
    customBackhalf = input('Backhalf (inputing "random" will create a 4 character random backhalf consisting of uppercase letters, lowercase letters, and digits.): ')
    print(' ')

    if customBackhalf == "random":
        backhalf = ( ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(4)) )
    else:
        backhalf = customBackhalf
    isdir = os.path.isdir(backhalf)

os.mkdir(backhalf)
file = open(f"{backhalf}/index.html","w+")
file.write(f'<meta http-equiv="refresh" content="0; URL={url}">')
file.close()
print(f'A short link created at "https://x.obvMath.com/{backhalf}". The short link has been copied to the clipboard.')
pyperclip.copy(f"https://x.obvMath.com/{backhalf}")

os.startfile("..\GitHubDesktop.exe.lnk") # Opens GitHub Desktop to remind me to push origin to GitHub Pages so the website actually updates.
print(' ')
print('Closing in:')
print('10')
time.sleep(1)
print('9')
time.sleep(1)
print('8')
time.sleep(1)
print('7')
time.sleep(1)
print('6')
time.sleep(1)
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
time.sleep(1)
quit()