#
#
#
# A script to generate fairly secure passwords
#
#
#

import random

wordFile = open("words.dat", 'r')
wordlist = wordFile.readlines()
replacements = (
('hacker', 'haxor'), ('elite', 'eleet'), ('a', '4'), ('e', '3'), ('l', '1'), ('o', '0'), ('t', '+'), ('/', ''))
alphabet = "abcdefghijklmnopqrstuvwxyz"
lst = ['!', '-', '=', '~', '|', '$', '.', ',', '@']
passcode = list()

# Define balancing method - adjust for your keyboard
def altscore(word):
	score = 0.0
	leftHand = "asdfgzxcvbqwert"
	rightHand = "lkjhpoiuymn"
	for i in range(len(word) - 1):
		if word[i] in leftHand and word[i + 1] in rightHand:
			score += 1
		elif word[i] in rightHand and word[i + 1] in leftHand:
			score += 1
	return score / (len(word) - 1)


# Define list of balanced words
goodwords = [word[:-1] for word in wordlist if altscore(word) >= 0.7]


# Define the function to Grab 4 random good words that total between 18 & 20 chars
def makePassword(goodwords):
	done = False
	while not done:
		passlist = []
		for i in range(4):
			passlist.append(goodwords[random.randrange(len(goodwords))])
		if len("".join(passlist)) <= 20 and len("".join(passlist)) > 18:
			done = True
	return ("/".join(passlist))


# Get list of words for password
mypwwords = makePassword(goodwords)

# Remove seperators into mypw variable
for old, new in replacements:
	mypw = mypwwords.replace(old, new)

# Get password length
pw_length = len(mypw)

# Add 1st password to the passcode list
passcode.insert(0, mypw)

# Randomise 4 words somewhat
# replace 1 or 2 characters with a number
for i in range(random.randrange(1, 5)):
	replace_index = random.randrange(len(mypw) // 2)
	mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index + 1:]

# replace 1 or 2 letters with an uppercase letter
for i in range(random.randrange(1, 5)):
	replace_index = random.randrange(len(mypw) // 2, len(mypw))
	mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1:]

# Add 2nd password to the passcode list
passcode.insert(1, mypw)

# The dreaded symbols added (Add 3rd password to the passcode list)
passcode.insert(2, "".join('%s%s' % (x, random.choice(lst) if random.random() > 0.8 else '') for x in mypw))

# Perform L33t transformation
# create and populate l33t variable
myl33tpw = passcode[0]
for old, new in replacements:
	myl33tpw = myl33tpw.replace(old, new)

# Add 4th password to the passcode list
passcode.insert(3, myl33tpw)

# The dreaded symbols added (Add 5th password to the passcode list)
passcode.insert(4, "".join('%s%s' % (x, random.choice(lst) if random.random() > 0.8 else '') for x in myl33tpw))

print("Word list")
print(mypwwords)
print("")
print("[0]: Combined word list")
print(passcode[0])
print("")
print("[1]: Randomised")
print(passcode[1])
print("")
print("[2]: With the dreaded symbols")
print(passcode[2])
print("")
print("[3]: L33t")
print(passcode[3])
print("")
print("[4]: With the dreaded symbols")
print(passcode[4])
print("")
# Ask user input

while True:
	selection = input("Select one (0-4) or anything else to quit:")
	if selection.lower() not in ('0', '1', '2', '3', '4'):
		print("Thanks.  Quitting & wiping memory...")
	else:
		if (selection == '0' or selection == '1' or selection == '2' or selection == '3' or selection == '4'):
			from tkinter import Tk
			r = Tk()
			r.withdraw()
			r.clipboard_clear()
			r.clipboard_append(passcode[int(selection)])
			r.destroy()
			print("")
			print("Password " + selection + " copied to clipboard.")
			break

# Blank password variables after use
mypwwords = 1
mypw = 1
myl33tpw = 1
passcode = 1
testVar = 1

# Check all vars are reset.
if (mypwwords + mypw + myl33tpw + passcode + testVar == 5):
	print("")
	print("All Shiney Cap'n.")
