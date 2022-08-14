name = input("Enter file name:")

# Open file
try:
    fileHandle = open(name)
except:
    print("Cannot open file " + name + " . Please enter an existing file name.")
    quit()

# Count words in file
wordsCount = dict()
for line in fileHandle:
    line = line.rstrip()
    if len(line) > 0:
        words = line.split(" ")
        for word in words:
            wordsCount[word] = wordsCount.get(word, 0) + 1

# Convert dictionary to list of tuples contain values and keys
wordsCountList = list()
for k, v in wordsCount.items():
    wordsCountList.append((v, k)) # append tuple into list

# Sort by count value desc
sortedWordsCount = sorted(wordsCountList, reverse=True)

# Print words count result
for k, v in sortedWordsCount:
    print(str(k) + ": " + v)
