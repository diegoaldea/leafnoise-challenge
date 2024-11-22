# Este codigo contempla tambien cuando se abre un parentesis dentro de otro

def brackets_detector(text):
    list_text = list(text)

    open_brackets_count = 0
    open_brackets = False
    balanced_brackets = False

    for character in list_text:
        if character == ")":
            if not open_brackets:
                return False
            else:
                open_brackets_count -= 1
                if open_brackets_count == 0:
                    open_brackets = False

        if character == "(":
            open_brackets_count += 1
            open_brackets = True

    if open_brackets_count == 0:
        balanced_brackets = True
    else:
        balanced_brackets = False

    return balanced_brackets

text = input("Escriba un texto: ")

if brackets_detector(text):
    print("parentesis balanceados")
else:
    print("parentesis NO balanceados")

input("Enter para cerrar")