msg = input(">")
word = msg.split(' ')
print(word)
emoji = {
    ":)" : "🙌",
    ":(" : "💕"
}
output = ''
for wor in word:
   output+= emoji.get(wor,wor) +""
   print(output)
    