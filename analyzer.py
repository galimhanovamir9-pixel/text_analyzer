# запрашиваем у пользователя текст
text = input('Введите слово или фразу:')
# считаем длинну текста
length = len(text.replace(" ", ""))
# выводим длинну текста
print(f'Длина слова: {length} букв')

# делаем очистку от пробелов и переводим в нижний регистр
purified = text.lower().replace(" ", "")
# проверяем на палиндром
if purified == purified[::-1]:
    print('Это палиндром')
else:
    print('Это не палиндром')

# создаем перемнную со всеми гласными
vowels = "аеёиоуыэюя"
vowels_number = 0
# создаем переменную с количеством согласных
consonants_number = 0
# перебираем гласные
for char in text.lower():
    if char in vowels:
        vowels_number += 1
# перебираем согласные
    elif char.isalpha():        
        consonants_number += 1

# выводим количество гласных
print(f'Количество гласных букв : {vowels_number}')
# выводим количество согласных
print(f'Количество согласных букв : {consonants_number}')
