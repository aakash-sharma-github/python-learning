# Day 47
# solution of encrypting and decrypting a message.
import random
# Taking input from user.
code = input("Enter \"1\" for encrypting and \"2\" for decrypting.")
str = input("Enter your message: ")

# randomly taking string from the list.
randList1 = ["gtd", "hfd", "kji", "lpo", "rea", "moy"]
randList2 = ["kgf", "kfc", "ipo", "tuf", "mkd", "rob"]

words = str.split(" ")
# condition as per user input.
code = True if (code == "1") else False

if code:
    newWord = []
    for word in words:
        if (len(word) >= 3): # if word is greater or equal to 3 letters then add random string and store it in newWord.
            ran1 = random.choice(randList1)
            ran2 = random.choice(randList2)
            newSTR = ran1 + word[1:] + word[0] + ran2
            newWord.append(newSTR)

# simply reverse the words.
        else:
            newWord.append(word[::-1])
    print(" ".join(newWord))

# if user wish to decrypt the message.
else:
    newWord = []
    for word in words:
        if (len(word) >= 3): # if word is greater or equal to 3 letters the 
            newSTR = word[3:-3] # this will remove the random string.
            newSTR = newSTR[-1] + newSTR[:-1] # this will rearrange the first letter that was added to last.
            newWord.append(newSTR)

# Rearrange the words.
        else:
            newWord.append(word[::-1])
    print(" ".join(newWord))