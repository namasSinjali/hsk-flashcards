chars = {}
with open('new-words.txt', encoding='utf-8') as hsk,  open("out.txt", 'w', encoding='utf-8') as out:
    lines = hsk.readlines()
    for line in lines:
        if line.startswith('//'):
            chars.setdefault(line.strip(), 0)
            chars[line.strip()]+=1
        else:
            for char in line:
                if char != '\n':
                    chars.setdefault(char, 0)
                    chars[char]+=1

    for el in chars:
        # out.write(f'{el}\t{chars[el]}\n')
        out.write(f'{el}\n')