import re

import fernet as fernet
from cryptography.fernet import Fernet
refid = input("Enter Referenceid : ")
print("original ref id: ", refid)
key = Fernet.generate_key()
fernet = Fernet(key)
x = True

while x:
    if (len(refid) != 12):
        break
    elif re.search("[$#@]",refid):
        break
    else:
        encrefid = fernet.encrypt(refid.encode())
        print("encrypted string: ", encrefid)
        decrefid = fernet.decrypt(encrefid).decode()
        print("decrypted string: ", decrefid)
        x=False
        break

if x:
    print("Not a Valid Ref id")


