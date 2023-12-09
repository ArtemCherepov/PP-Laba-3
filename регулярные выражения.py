import re

while True:
    #XXX-XXX-XXX XX
    reg = r'^(\d{3})(\-)(\d{3})(\-)(\d{3})(\s)(\d{2})$'
    string = input("Введите СНИЛС: ")
    match = re.search(reg, string)
    if match == None:
        print("СНИЛС введен неправильно")
    else:
        print(match)
        break

