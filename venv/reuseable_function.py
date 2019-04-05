
def enoji_convertor(msg):
        word = msg.split(' ')
        print(word)
        emoji = {
        ":)": "🙌",
        ":(": "💕"
        }
        output = ''
        for wor in word:
            output += emoji.get(wor, wor) + ' '
        return output


msg = input(">")
print(enoji_convertor(msg))
