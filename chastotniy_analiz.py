from operator import itemgetter

# vhod = open('vhod.txt', 'r')
# slovo = vhod.read().lower()
# vhod.close()
slovo = input("Введите слово: ")
slovo = list(slovo)
phrase = list(slovo)

abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
chastota = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', 'я', 'ы', 'ь', 'г', 'з', 'б', 'ч', 'й', 'х']


def top_letter_detect(phrase):
    top = 0
    top_letter = {}
    for i in abc:
        if phrase.count(i) > top:
            top = phrase.count(i)
            top_letter[i] = phrase.count(i)
    top_letter = list(map(list, dict(sorted(top_letter.items(), key=itemgetter(1))).items()))
    return top_letter


def find_sdvig(top_letter):
    sdvig = 0
    x = -1
    while sdvig == 0:
        sdvig = abc.index(top_letter[x][0]) - abc.index(chastota[x*(-1) - 1])
        x -= 1
    print('Ключ:', sdvig)
    return sdvig


def encrypt(sdvig):
    rez = []
    for i in range(len(phrase)):
        if phrase[i] in abc:
            y = abc.index(phrase[i]) - sdvig
            if y > 32:
                y -= 33
            rez += abc[y]
        else:
            rez += phrase[i]
    print('Вывод: ')
    return rez


print(''.join(encrypt(find_sdvig(top_letter_detect(phrase)))))
