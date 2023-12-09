import re

#Регулярное выражение
#XXX-XXX-XXX XX
reg = r'^(\d{3})(\-)(\d{3})(\-)(\d{3})(\s)(\d{2})$'
string = input("Введите СНИЛС: ")
match = re.search(reg, string)
print(match)
