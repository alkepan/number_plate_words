from english_words import get_english_words_set

wordListOG = get_english_words_set(['gcide'], lower=True)

wordListNew = []

for word in wordListOG:
    wordListNew.append(word)
wordListNew.sort()

fiveLetterList = []

for word in wordListNew:
    if len(word) == 5:
        word = word.upper()
        fiveLetterList.append(word)

lettNums = ("I","L","Z","E","A","S","T","B","G","O")

foundWords = []

for word in fiveLetterList:
    if word[1] in lettNums and word[2] in lettNums:
        foundWords.append(word)

removeWords = []

for word in foundWords:
    if word[1] == "I" and word[2] == "L":
        removeWords.append(word)

for word in foundWords:
    if word[1] == "L" and word[2] == "I":
        removeWords.append(word)


for word in removeWords:
    if word in foundWords and removeWords:
        foundWords.remove(word)

wordsList = []

for word in foundWords:
    listWord = list(word)
    wordsList.append(listWord)

for word in wordsList:
    if word[1] == "I":
        word[1] = "1"
    elif word[1] == "L":
        word[1] = "1"
    elif word[1] == "Z":
        word[1] = "2"
    elif word[1] == "E":
        word[1] = "3"
    elif word[1] == "A":
        word[1] = "4"
    elif word[1] == "S":
        word[1] = "5"
    elif word[1] == "T":
        word[1] = "7"
    elif word[1] == "B":
        word[1] = "8"
    elif word[1] == "G":
        word[1] = "9"
    elif word[1] == "O":
        word[1] = "0"   
    if word[2] == "I":
        word[2] = "1"
    elif word[2] == "L":
        word[2] = "1"
    elif word[2] == "Z":
        word[2] = "2"
    elif word[2] == "E":
        word[2] = "3"
    elif word[2] == "A":
        word[2] = "4"
    elif word[2] == "S":
        word[2] = "5"
    elif word[2] == "T":
        word[2] = "7"
    elif word[2] == "B":
        word[2] = "8"
    elif word[2] == "G":
        word[2] = "9"
    elif word[2] == "O":
        word[2] = "0"

numsOnPlate = []

for list1 in wordsList:
    list2 = ''.join(list1)
    numsOnPlate.append(list2)

i = 0

while i < len(numsOnPlate):
    print(numsOnPlate[i] , foundWords[i] , i + 1)
    i += 1

input()
