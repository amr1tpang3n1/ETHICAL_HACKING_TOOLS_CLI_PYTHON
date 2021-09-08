import hashlib
hashToCrack = input("Enter a hash to decode:")
filePath = input("Enter Path to dictionary File: ")
print("Select Hash Algorithm:\n 1. Md5 \n 2. Sha256")
hashType = input("Response: ")
try:
    dictionaryFile = open(filePath, 'r')
    # This statement will print every line in the file
    passwordList = []
    for x in dictionaryFile:
        x = x.strip()
        passwordList.append(x)

    if hashType.strip() == "1":
        for i in passwordList:
            password = i.encode()
            passwordHash = hashlib.md5(password).hexdigest()
            if passwordHash == hashToCrack:
                print(f"Password Found:\n hash = {passwordHash} \n Plain Text = {i}")
                break
    elif hashType.strip() == "2":
        for i in passwordList:
            password = i.encode()
            passwordHash = hashlib.sha256(password).hexdigest()
            if passwordHash == hashToCrack:
                print(f"Password Found:\n hash = {passwordHash} \n Plain Text = {i}")
                break

except Exception:
    print("No Such file !")