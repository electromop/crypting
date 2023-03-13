sdvig = int(input("Введите сдвиг шифра: "))
# vhod = open('vhod.txt', 'r')
# slovo = vhod.read().lower()
# vhod.close()
slovo = input("Введите слово: ")
slovo = list(slovo)
op_type = str(input("Введите тип операции(crypt/encrypt): "))

abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
rez = []

for i in range(len(slovo)):
    if slovo[i] in abc:
        x = slovo[i]
        if op_type == 'crypt':
            y = abc.index(x) + sdvig
        elif op_type == 'encrypt':
            y = abc.index(x) - sdvig
        if y > 32:
            y -= 33
        rez += abc[y]
    else:
        rez += slovo[i]

print('Вывод: ')
print(''.join(rez))
