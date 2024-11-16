print("love calculator💚")
name1 = str(input("Please enter your name: "))
name2 = str(input("Please enter your crush's name😍: "))
word1 = "true"
word2 = "love"
combined_name = name1 + name2
count1 = 0
count2 = 0
for symbol in combined_name:
    if symbol in word1:
        count1 += 1
    if symbol in word2:
        count2 += 1

score = int(str(count1) + str(count2))
if score < 10 or score > 90:
    print("Your score is", score, "you go together like coke and mentos.")
elif score > 40 and score < 50:
    print("Your score is", score, "you are alright together.")
else:
    print("Your score is", score)
