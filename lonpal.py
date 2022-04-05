words=open('/storage/emulated/0/Python stuff/words.txt',mode='r')
words.seek(0)
wordlist=words.read().splitlines()
valwords=[]
banchars='acdfgjkmnpqruvwxyz'
cban=0
for word in wordlist:
    cban=0
    for char in word:
        if char in banchars:
            cban=1
    if (cban==0) and (word==word[::-1]):
        valwords.append(word)
valwords.sort(key=len)
valwords.reverse()
valwords=valwords[:10]
print(valwords)
words.close()