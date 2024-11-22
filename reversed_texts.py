def text_reverser(text):
    words = []
    text_reversed = []

    word = ""
    count = 0
    for letter in text:
        if letter == " " or letter == ",":
            words.append(word)
            if letter == ",":
                words.append(",")
            word = ""
        elif count == len(text) - 1:
            word += letter
            words.append(word)
        else:
            word += letter
        count += 1        

    text_reversed = " ".join(words[::-1])

    return text_reversed

text = input("Te invierto lo que escribas a continuacion: ")

print(text_reverser(text))

input("Enter para cerrar")