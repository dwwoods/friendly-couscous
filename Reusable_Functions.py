#reorgansie emoji_converer.py exercise into a function

def emoji_converter(message_emoji2):
    words_emoji2 = message_emoji2.split(" ")
    emojis = {
    ":)" : "😁",
    ":(" : "😒"

    }
    output = ""
    for word in words_emoji2:
            output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))



