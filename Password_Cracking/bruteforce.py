# Brute Force Offline Password Hash Cracking Attack Simple Logic
import hashlib
hashToCrack = input("Enter a Hash to decode: ")
print("Enter Hash Algorithm type:\n 1. Md5 \n 2. Sha256")
hashType = input("Response:")

if hashType.strip() == "1" or hashType.strip() == "2":
    pass
else:
    print("Hash Algorithm you trying to select isn't supported")
    exit()

print("Select Modes:\n 1. Alphabets \n 2. Digits")
mode = input("Response:")

finalCharset = ["abcdefghijklmnopqrstuvwxyz","1234567890"]
if mode.strip() == "1":
    finalCharset = finalCharset[0]
elif mode.strip() == "2":
    finalCharset = finalCharset[1]
else:
    print("Mode you trying to access doesn't exist")
    exit()

minLength = int(input("Minimum Length: "))
maxLength = int(input("Maximum Length: "))

wordList = []
for i in range(int(minLength) - 1, int(maxLength)):
    passwordGenerated = [i for i in finalCharset]
    for j in range(i):
        passwordGenerated = [j + i for i in finalCharset for j in passwordGenerated]
    wordList = wordList + passwordGenerated

if hashType.strip() == "1":
    for i in wordList:
        password = i.encode()
        passwordHash = hashlib.md5(password).hexdigest()
        if passwordHash == hashToCrack:
            print(f"Password Found:\n hash = {passwordHash} \n Plain Text = {i}")
            break

elif hashType.strip() == "2":
    for i in wordList:
        password = i.encode()
        passwordHash = hashlib.sha256(password).hexdigest()
        if passwordHash == hashToCrack:
            print(f"Password Found:\n hash = {passwordHash} \n Plain Text = {i}")
            break