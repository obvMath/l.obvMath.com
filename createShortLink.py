# This is used on the backend to create short links.

import random
import string
import os
import pyperclip
from datetime import datetime
import time

linkName = input('Link Name: ')

# Checks if URL entered is valid (starts with http:// or https://)
isUrlValid = False
while isUrlValid == False:
    print(' ')
    url = input('URL to redirect to: ')
    if url.startswith('https://') or url.startswith('http://'):
        isUrlValid = True
    else:
        isUrlValid = False

# Checks if short link already exists
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

os.mkdir(backhalf) # Creates folder
file = open(f"{backhalf}/index.html","w+") # Created HTML file in folder
file.write(f'<meta http-equiv="refresh" content="0; URL={url}">') # Writes redirect code to HTML file
file.close() # Saves the file

timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
record = open("links/index.html", "a")
record.write(f'\n<tr><td>{linkName}</td><td>{timestamp}</td><td>{backhalf}</td><td><a href="{url}" target="_blank">{url}</a></td></tr>')
record.close

print(f'A short link created at "https://x.obvMath.com/{backhalf}". The short link has been copied to the clipboard.') # Confirmation that short link was created
pyperclip.copy(f"https://x.obvMath.com/{backhalf}") # Copies created short link to clipboard

os.startfile("..\GitHubDesktop.exe.lnk") # Opens GitHub Desktop to remind me to push origin to GitHub Pages so the website actually updates.
print(' ')
print('Closing in:')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Closing...')
time.sleep(1)
quit()