minLength = int(input("Minimum Length: "))
maxLength = int(input("Maximum Length: "))
finalCharset = input("Characters to include on dictionary (Charset): ")

wordList = []
for i in range(int(minLength) - 1, int(maxLength)):
    passwordGenerated = [i for i in finalCharset]
    for j in range(i):
        passwordGenerated = [j + i for i in finalCharset for j in passwordGenerated]
    wordList = wordList + passwordGenerated

dictionary_file = open('dictionary.txt', 'a')
for i in wordList:
    dictionary_file.write(f"{i}\n")

dictionary_file.close()