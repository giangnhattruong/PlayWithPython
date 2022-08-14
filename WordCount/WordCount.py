from pickle import TRUE


name = input("Enter file name:")

try:
    fileHandle = open(name)
except:
    print("Cannot open file " + name + " . Please enter an existing file name.")
    quit()

wordsCount = dict()

for line in fileHandle:
    words = line.strip().split(" ")
    for word in words:
        wordsCount[word] = wordsCount.get(word, 0) + 1

wordsCountList = list()

for k, v in wordsCount.items():
    wordsCountList.append((v, k))

sortedWordsCount = sorted(wordsCountList, reverse=True)

for k, v in sortedWordsCount:
    print(str(k) + ": " + v)
