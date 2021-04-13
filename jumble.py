from english_words import english_words_set as dictwords
scrambleword=input("enter your scrambled word ")
mixedword=set(scrambleword)
for word in dictwords:
    if mixedword==set(word):
        print ("possible word:",word)
