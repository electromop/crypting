import pandas as pd

phrase = list(input().lower())
abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

chastota = pd.read_csv('chastota.csv', index_col=1)
chastota.head()

top_dict = {}

def top_of_letters(x):
    for i in range(len(abc)):
        top_dict[abc[i]] = round((x.count(abc[i])/len(x))*100, 5)
    return top_dict

print(top_of_letters(phrase))
