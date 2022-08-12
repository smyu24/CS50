from cs50 import get_string

text = get_string("Text: ")
counter = 0
for i in text:
    counter += 1
words = 0
sents = 0
letters = 0
for i in range(counter):
    if ord (text[i])>=65 and ord(text[i]) <= 122:
        letters += 1
    elif ord (text[i]) == 32 and ord (text[i - 1]) != 33 and ord (text[i - 1]) != 46 and ord (text[i - 1]) != 63:
        words += 1
    elif ord (text[i]) == 33 or ord (text[i]) == 46 or ord (text[i]) == 63:
        words += 1
        sents += 1
print(str(letters) + " " + str(words) + " " + str(sents))
avgL = letters
avgS = sents

total = 0.0588 * (100 * float(avgL) / float(words))- 0.296 * (100 * float(avgS) / float(words)) - 15.8 
if total < 16 and total >= 0:
    print("Grade: " + str(round(total)))
elif total >= 0:
    print("Grade 16+")
else:
    print("Before Grade 1")

