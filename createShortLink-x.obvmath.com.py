# This is used on the backend to create short links.

import random
import string
import os

url = input('URL to redirect to: ')
print(' ')
backhalf = input('Backhalf (inputing "random" will create a 4 character random backhalf consisting of uppercase letters, lowercase letters, and digits.): ')

if backhalf == "random":
    randomBackHalf = ( ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(4)) )
    os.mkdir(randomBackHalf)
    file = open(f"{randomBackHalf}/index.html","w+")
    file.write(f'<meta http-equiv="refresh" content="0; URL={url}">')
    file.close()
else:
    os.mkdir(backhalf)
    file = open(f"{backhalf}/index.html","w+")
    file.write(f'<meta http-equiv="refresh" content="0; URL={url}">')
    file.close()