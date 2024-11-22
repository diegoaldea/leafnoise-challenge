def is_palindrome(text):
    list_text = list(text) # convierto el texto en una lista para poder iterar

    count = 0
    for letter in list_text:
        if letter == " " or letter == ",": # si el texto tiene espacio o comas
            list_text[count] = "" # lo cambio por un caracter vacio
        count += 1

    text = ''.join(list_text).lower() # uno la cadena en los caracteres vacios

    if text == text[::-1]: # comparo si la cadena es igual en ambos sentidos
        return True
    else:
        return False

text = input("Escribi una palabra o texto y te digo si es palíndromo o no (sin tildes): ")

if is_palindrome(text):
    print("El texto es palíndromo")
else:
    print("El texto NO es palíndromo")