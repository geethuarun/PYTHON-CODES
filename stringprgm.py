# text="one 100 and fifty 5"
# texts=text.split(" ")
# for w in texts:
#     if w.isdigit():
#         print(w)

# digit=[w for w in texts if w.isdigit()]
# print(digit)


text="england promise to continue its aggresive approach to test cricket "
#print first word with vowel
word=text.split(" ")

v={"a","e","i","o","u"}
for w in text.split():
    if w[0].casefold() in v:
         print(w)


# longest word
# text="hello i am here in maravanchery"
# word=text.split(" ")
# print(word)


# print(max(text,key=lambda w:len(w)))
