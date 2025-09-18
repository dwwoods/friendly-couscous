message_emoji = input(">")
words_emoji = message_emoji.split(" ")
emojis = {
    ":)" : "😁",
    ":(" : "😒"

}
output = ""
for word in words_emoji:
    output += emojis.get(word, word) + " "
print(words_emoji)
print(output)


