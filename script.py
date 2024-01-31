import argparse, sys, os

parser = argparse.ArgumentParser()

hskCategories = ['1', '2', '3', '4a', '4b', '4']

parser.add_argument('actions', nargs='*', choices=['newwords', 'newcharacters', 'heisig'])
parser.add_argument('--hskfromto', nargs=2, choices=hskCategories)
parser.add_argument('--hsklevels', nargs='+', choices=hskCategories)

args = parser.parse_args()

hskSelected = set()

if args.hskfromto:
    doAppend = False
    for cat in hskCategories:
        if cat == args.hskfromto[0]:
            doAppend = True
        
        if doAppend:
            hskSelected.add(cat)

        if cat == args.hskfromto[1]:
            doAppend = False

if args.hsklevels:
    for level in args.hsklevels:
        hskSelected.add(level)

if not (args.hsklevels or args.hskfromto):
    hskSelected.update(hskCategories)

if '4' in hskSelected:
    hskSelected.add('4a')
    hskSelected.add('4b')
    hskSelected.remove('4')

if not os.path.exists('out'):
    os.makedirs('out')

hskList = {}
with open('new-words.txt', encoding='utf-8') as hskFile:
    lines = hskFile.readlines()
    currList = []

    for line in lines:
        if line.startswith('//'):
            hskNo = line[-6]
            lessonNo = line[-3:-1]

            hskList.setdefault(hskNo, {})

            currList = []

            if(hskNo == '4'):
                categ = '4a' if int(lessonNo) <=10 else '4b'
                hskList[hskNo].setdefault(categ, {})
                hskList[hskNo][categ].setdefault(lessonNo, currList)
            else:
                hskList[hskNo].setdefault(lessonNo, currList)
        else:
            currList.append(line.rstrip())

filteredWords = {}
for hskNo in ['1', '2', '3', '4']:
    if any(hskNo == a[0] for a in hskSelected):
        subcateg = hskList[hskNo]
        if len(subcateg) == 2:
            for l in ['a', 'b']:
                if hskNo+l in hskSelected:
                    filteredWords.setdefault(hskNo, {})
                    filteredWords[hskNo] = {**filteredWords[hskNo], **hskList[hskNo][hskNo+l]}
        else:
            filteredWords[hskNo] = hskList[hskNo]

if not args.actions or 'newwords' in args.actions:
    with open('out/new-words.txt', 'w', encoding='utf-8') as out:
        for hskNo, lessons in filteredWords.items():
            for lessonNo, words in lessons.items():
                out.write(f'//New Words/HSK{hskNo}/HSK{hskNo}_L{lessonNo}\n'+'\n'.join(words)+'\n')

if not ('newcharacters' in args.actions or 'heisig' in args.actions):
    sys.exit()

filteredCharacters = {}
chars = {}
for hskNo in filteredWords:
    currHsk = {}
    filteredCharacters[hskNo] = currHsk
    for lessonNo in filteredWords[hskNo]:
        currLesson = []
        currHsk[lessonNo] = currLesson
        for words in filteredWords[hskNo][lessonNo]:
            for word in words:
                for char in word:
                    chars.setdefault(char, 0)
                    chars[char]+=1
                    if chars[char] == 1:
                        currLesson.append(char)

if 'newcharacters' in args.actions:
    with open('out/new-characters.txt', 'w', encoding='utf-8') as out:
        for hskNo, lessons in filteredCharacters.items():
            for lessonNo, chars in lessons.items():
                out.write(f'//New Characters/HSK{hskNo}/HSK{hskNo}_L{lessonNo}\n'+'\n'.join(chars)+'\n')

if not 'heisig' in args.actions:
    sys.exit()

allChars = []
for lessons in filteredCharacters.values():
    for lesson in lessons.values():
        allChars.extend(lesson)

with open('Rsh_v2.txt', encoding='utf-8') as rshfile:
    rshChars = []
    rshLines = []
    lines = rshfile.readlines()
    for line in lines:
        if not line.startswith('//'):
            rshLines.append(line.rstrip())
            rshChars.append(line[0])

filteredRsh = []
for i, char in enumerate(rshChars):
    if char in allChars:
        filteredRsh.append(rshLines[i])

with open('out/RSHxHSK.txt', 'w', encoding='utf-8') as out:
    out.write('//RSHxHSK\n'+'\n'.join(filteredRsh))