import hashlib
string = input("Enter a string to generate hash: ")
print("Select Hash Algorithm:\n 1. Md5 \n 2. Sha256")
hashType = input("Response: ")

if hashType.strip() == "1":
    password = string.encode()
    passwordHash = hashlib.md5(password).hexdigest()
    print(passwordHash)
elif hashType.strip() == "2":
    password = string.encode()
    passwordHash = hashlib.sha256(password).hexdigest()
    print(passwordHash)
else:
    print("Option Unavailable !")